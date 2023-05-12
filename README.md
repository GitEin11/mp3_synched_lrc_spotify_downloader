Downloads mp3 and synched lyrics (with jap to romaji, kor to romaja, chi to pinyin translation) from currently playing song on spotify client

Requirements:

```
pip3 install --upgrade spotify-cli
pip install spotdl
sudo apt install util-linux
pip install langid
pip install cutlet
cargo install pinyin-tool
pip3 install syrics
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
sudo apt-get update && sudo apt-get install spotify-client
```

build and install kroman from https://github.com/victorteokw/kroman
```
git clone https://github.com/victorteokw/kroman.git
cd kroman
make install
```

add lines in your ~/.bashrc to be able to change terminal title thru cli, see attached "./add to .bashrc" file


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

![1](https://github.com/GitEin11/mp3-synched-lrc-spotify-downloader/assets/84138811/8338ab89-bcd3-496d-970f-5fde60794dc9)


![2](https://github.com/GitEin11/mp3-synched-lrc-spotify-downloader/assets/84138811/fd4d0773-a58c-46dc-b6df-26a0516fa9fa)


![3](https://github.com/GitEin11/mp3-synched-lrc-spotify-downloader/assets/84138811/aabf2eb7-6481-49d0-8f50-203b0230e043)


![4](https://github.com/GitEin11/mp3-synched-lrc-spotify-downloader/assets/84138811/0e55fcd3-a9ce-42f1-987b-52ed93b4e363)

https://github.com/GitEin11/script-for-spotify-mp3-and-synched-lyrics-downloader/assets/84138811/33ecb6fa-0ac2-491b-a4c6-76a0d6f3d52e
