Downloads mp3 and synched lyrics (with jap to romaji, kor to romaja, chi to pinyin translation) from currently playing song on spotify client

>I'm using ubuntu 20.04, doesnt work on 22.04 I'm having issue with cli module of spotify-cli

Requirements:

```
pip3 install --upgrade spotify-cli        # control spotify thru cli
pip install spotdl                        # downloads mp3
pip install langid                        # for language detection
pip install cutlet                        # Jap to Romaji
pip install unidic-lite                   # Jap dictionary
pip3 install syrics                       # downloads lyrics from spotify
```
>you need to configure syrics sp_dc, go to the developers page https://github.com/akashrchandran/syrics for instruction
>
>after getting sp_dc you can configure it via cli, or just edit the file here ~/.config/syrics/config.json

```
sudo apt install util-linux cargo         # for typescript and installation of pinyin-tool
cargo install pinyin-tool                 # Chi to Pinyin
sudo cp ~/.cargo/bin/pinyin-tool /usr/bin # copy pinyin-tool to /usr/bin
```

Install spotify client but not the snap version
https://www.spotify.com/us/download/linux/

configure debian repository:
```
curl -sS https://download.spotify.com/debian/pubkey_7A3A762FAFD4A51F.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
```
install the Spotify client:
```
sudo apt update && sudo apt install spotify-client
```

build and install kroman from https://github.com/victorteokw/kroman
```
# Kor to Romaja
git clone https://github.com/victorteokw/kroman.git
cd kroman
sudo make install
```

for the setup of spotify-cli

from https://github.com/ledesmablt/spotify-cli

You may also pass [your own Spotify application](https://developer.spotify.com/dashboard/applications)'s
client ID and secret if you want to track your usage or avoid
API rate limiting issues (all users using the default client settings share the same rate limits).

When doing so, please ensure that [this URL](https://asia-east2-spotify-cli-283006.cloudfunctions.net/auth-redirect)
is listed as a Redirect URI in your application.
```
$ spotify auth login --client-id XXXXX --client-secret YYYYY
```
      
Also put a client ID/Secret on "./Spotify downloader" for spotdl

You must also get a Musixmatch token, no need to register
to do that install Musixmatch
```
sudo snap install musixmatch
```
then run in via terminal,
```
musixmatch
```
and look for the "userToken":"TOKEN HERE"
put the token into ./data/LyrMusixmatch

make sure all the scripts are executable

sources:
https://github.com/ledesmablt/spotify-cli https://github.com/spotDL/spotify-downloader https://github.com/saffsd/langid.py https://github.com/polm/cutlet https://github.com/briankung/pinyin-tool https://github.com/victorteokw/kroman https://github.com/akashrchandran/syrics https://gist.github.com/blueset/43172f5ecd32e75d9f9bc6b7e0177755 https://github.com/fashni/MxLRC


Now all you need to do is play a song in your spotify client and run ./Spotify downloader in terminal

note: spotify command is replaced by spotify-cli, to launch the client use /usr/bin/spotify as your command this is applied upon reboot

![1](https://github.com/GitEin11/mp3-synched-lrc-spotify-downloader/assets/84138811/8338ab89-bcd3-496d-970f-5fde60794dc9)


![2](https://github.com/GitEin11/mp3-synched-lrc-spotify-downloader/assets/84138811/fd4d0773-a58c-46dc-b6df-26a0516fa9fa)


![3](https://github.com/GitEin11/mp3-synched-lrc-spotify-downloader/assets/84138811/aabf2eb7-6481-49d0-8f50-203b0230e043)


![4](https://github.com/GitEin11/mp3-synched-lrc-spotify-downloader/assets/84138811/0e55fcd3-a9ce-42f1-987b-52ed93b4e363)

https://github.com/GitEin11/script-for-spotify-mp3-and-synched-lyrics-downloader/assets/84138811/33ecb6fa-0ac2-491b-a4c6-76a0d6f3d52e



*If the language is not included here, you can ask chatGPT or any language model of your choice to do the romanization

example: this song from BABYMETAL PA PA YA!! has thai language in it
```
me:
romanized this
[02:26.17]Rap Rap หมอลำ Rock Rock
[02:27.46]สุดแต่ชะตาจะมาเคาะ ก๊อก ก๊อก
[02:28.92]เพราะชีวิตเหมือน Chocolate Box Box
[02:30.49]มีผสมกันเหมือน Papaya Pok Pok
[02:31.93]โดน Knock Knock Knock ล้มๆลุกๆ
[02:33.22]โขลกๆความสุขไปกับทุกข์ๆๆ
[02:34.87]มะละกอโดนทุบๆๆ
[02:36.33]ถึงจะแซ่บ ถึงจะนัว ถึงจะกรอบกรุ้บๆ
[02:38.03]ซิ่งรถตุ๊กๆ อย่าง Thai Rider
[02:39.64]Hot and Spicy เพราะนี่ Summer
[02:41.14]I was Lightning Before the Thunder
[02:42.69]ส้มตำ ปลาดิบ เฮามาม่วนกันเด้อ
[02:44.19]Baby Girls, ฮานาก้า
[02:45.69]สั่งบิกินี่มาจาก Lazada
[02:47.26]Jumpin' in the Pool La La La
[02:48.76]แสงแดดแผดเผาเรามา Papaya
```
```
ChatGPT:
"[02:26.17]Rap Rap mor lam Rock Rock
[02:27.46]sut tae cha dta ja ma kao kork kork
[02:28.92]por chii wit meuuan Chocolate Box Box
[02:30.49]mii pha som gan meuuan Papaya Pok Pok
[02:31.93]dohn Knock Knock Knock lom lom luk luk
[02:33.22]khlo khlo khwam suk bpai kap thuk-thuk
[02:34.87]ma la kor dohn thub thub thub
[02:36.33]teung ja saeb, teung ja nua, teung ja krop kroob kroob
[02:38.03]sing roht dtook dtook yahng Thai Rider
[02:39.64]Hot and Spicy por nee Summer
[02:41.14]I was Lightning Before the Thunder
[02:42.69]som tam, pla dip, hao ma muan gan der
[02:44.19]Baby Girls, Hanaka
[02:45.69]sang bignii mah jak Lazada
[02:47.26]Jumpin' in the Pool La La La
[02:48.76]saeng daet paet pao rao mah Papaya"

This is the romanized version of the provided Thai lyrics.
```
