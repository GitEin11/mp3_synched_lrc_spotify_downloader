import requests
import argparse
import os
import re
import json
import mutagen
import base64
from mutagen import easyid3
import sys
from Crypto.Cipher import AES
from collections import defaultdict

def get_song_id(enc):
    enc = enc[22:]
    unpad = lambda s: s[:-ord(s[len(s)-1:])]
    enc = base64.b64decode(enc)
    iv = enc[:16]
    key = "#14ljk_!\]&0U<'(".encode()[:16]
    cipher = AES.new(key, AES.MODE_ECB, iv)
    data = unpad(cipher.decrypt(enc))[6:].decode()
    return json.loads(data)['musicId']

arg = argparse.ArgumentParser()
arg.add_argument("query", help="Search query or Song ID or File name\n"
                               "Search query or Song ID: output file\n"
                               "File name: LRC to filename.lrc\n"
                               "Query is extracted from IRC tag")
arg.add_argument("-m", "--mode",
                 help="Mode of LRC file",
                 choices=["trans", "original", "both"],
                 default="both")
arg.add_argument("-f", "--format",
                 help="Format to combine both types of lyrics\n"
                      "Default: \"{orig} / {trans}\"",
                 default="{orig} / {trans}")
arg.add_argument("-q", "--quiet",
                 help="Quiet mode, no prompt output to STDOUT, choose first search result by default.",
                 action='store_true')
arg.add_argument("-d", "--default",
                 help="Choose first search result by default.",
                 action='store_true')
arg.add_argument("-o", "--output",
                 help="Output file, - for STDOUT",
                 type=str,
                 default=None)

sn = requests.Session()
sn.headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36",
                  "Referer": "http://music.163.com/search/"})

search = 'http://music.163.com/api/search/get'

ap = arg.parse_args()

query = ap.query

ap.default |= ap.quiet


def qprint(*args, **kwargs):
    global ap
    if not ap.quiet:
        print(*args, **kwargs)

if os.path.isfile(ap.query):

    id3 = easyid3.EasyID3(ap.query)
    query = "%s %s" % ((id3['title'] + [''])[0], (id3['artist'] + [''])[0])
    mutf = mutagen.File(ap.query)
    if 'COMM::XXX' in mutf.keys() and mutf['COMM::XXX'].text[0].startswith("163 key(Don't modify):"):
        query = str(get_song_id(mutf['COMM::XXX'].text[0]))
        qprint("Found music file from Netease, ID:", query)
    qprint("Searching \"%s\"\n" % query)
    if ap.output is None:
        output = ".".join(ap.query.split('.')[:-1]) + ".lrc"
    else:
        output = ap.output
else:
    if ap.output is None:
        qprint("No output spicified, stdout used.")
        output = '-'
    else:
        output = ap.output

res = sn.post(search, data={
    "s": query,
    "type": 1,
    "offset": 0,
    "limit": 10
}).json()

songs = res['result']['songs']
if len(songs) == 0:
    qprint("No result found for \"%s\"." % query)
    exit()
elif len(songs) == 1 or ap.default:
    song = songs[0]['id']
    sid = 0
else:
    qprint("Choose a song to download, or ^C to exit.\n")
    for i, s in enumerate(songs):
        qprint("%-5s\x1b[1m%s\x1b[0m \x1b[2m(%d)\x1b[0m" % ("%s." % i, s['name'], s['id']))
        qprint("     \x1b[0m%s | \x1b[3m%s\x1b[0m" %
              ("; ".join([j['name'] for j in s['artists']]), s['album']['name']))
        qprint()
    sid = input("Song ID: ")
    while not sid.isdecimal() or int(sid) < 0 or int(sid) >= len(songs):
        qprint("%s is invalid. Please enter a integer between 0 and %s." % (sid, len(songs)))
        sid = input("Song ID: ")
    sid = int(sid)
    song = songs[int(sid)]['id']

songinfo = [songs[sid]['name'], "; ".join([j['name'] for j in songs[sid]['artists']]), songs[sid]['album']['name']]

songstr = "     \x1b[1m%s\x1b[0m \x1b[2m(%d)\x1b[0m\n" % (songinfo[0], songs[sid]['id'])
songstr += "     \x1b[0m%s | \x1b[3m%s\x1b[0m\n" % (songinfo[1], songinfo[2])

qprint()
qprint("Trying to download song %s:" % song)
qprint(songstr)
req = sn.get("http://music.163.com/api/song/lyric?lv=1&kv=1&tv=-1&id=%s" % song).json()



if req.get('lrc', None) is None or req['lrc'].get('lyric', None) is None:
    qprint("No lyrics found.")
    exit()

has_trans = True

if ap.mode in ['trans', 'both']:
    if req.get('tlyric', None) is None or req['tlyric'].get('lyric', None) is None:
        qprint("No translation found, fallback to original lyrics.")
        has_trans = False
        ap.mode = 'original'
else:
    has_trans = False

org = defaultdict(str)
trans = defaultdict(str)

r = re.compile(r"\[(?P<tag>[0-9:.\]\[]+)\](?P<lrc>.*)")

for i in req['lrc']['lyric'].split('\n'):
    rm = r.match(i)
    if not rm:
        continue
    ln = rm.groupdict()
    for j in ln['tag'].split(']['):
        org[j] = ln['lrc'].strip()

if has_trans:
    for i in req['tlyric']['lyric'].split('\n'):
        rm = r.match(i)
        if not rm:
            continue
        ln = rm.groupdict()
        for j in ln['tag'].split(']['):
            trans[j] = ln['lrc'].strip()

out = []
for i in sorted(org):
    if ap.mode == 'original' or not trans[i].strip() or trans[i].strip() == org[i].strip():
        line = ["[{tag}]{orig}"]
    elif ap.mode == 'trans' or not org[i].strip():
        line = ['[{tag}]{trans}']
    elif ap.mode == 'both':
        line = ['[{tag}]' + i for i in ap.format.split('\n')]
    for l in line:
        out.append(l.format(tag=i, orig=org[i], trans=trans[i]))

if output == "-":
    of = sys.stdout
else:
    of = open(output, 'w')

with of:
    of.write("\n".join(out))

if output != '-':
    qprint('Done')
