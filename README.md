Requirements:

```
pip3 install --upgrade spotify-cli
pip install spotdl
sudo apt install util-linux
pip3 install py3langid
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

add lines for your ~/.bashrc to be able to change terminal title thru cli, see attached "add to .bashrc" file

for setup spotify-cli from https://github.com/ledesmablt/spotify-cli
You may also pass [your own Spotify application](https://developer.spotify.com/dashboard/applications)'s
client ID and secret if you want to track your usage or avoid
API rate limiting issues (all users using the default client settings share the same rate limits).

When doing so, please ensure that [this URL](https://asia-east2-spotify-cli-283006.cloudfunctions.net/auth-redirect)
is listed as a Redirect URI in your application.
```
$ spotify auth login --client-id XXXXX --client-secret YYYYY
```
      
Also put your a client ID/Secret on "./Spotify downloader" for spotdl

make sure all the scripts are executable


Now all you need to do is play a song in your spotify client and run in terminal ./Spotify downloader
all other description is commented in their respective script.


https://github.com/GitEin11/script-for-spotify-mp3-and-synched-lyrics-downloader/assets/84138811/33ecb6fa-0ac2-491b-a4c6-76a0d6f3d52e
