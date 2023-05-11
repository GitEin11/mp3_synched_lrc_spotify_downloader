# Play a song from spotify, run the script

Prereq list.

1. install spotify client but not the snap version see https://www.spotify.com/us/download/linux/

2. ```
pip3 install --upgrade spotify-cli #from https://github.com/ledesmablt/spotify-cli to get datas from spotify thru cli also take note of CLIENT ID and SECRET explained in there website
```

3. ```pip install spotdl```

from https://github.com/spotDL/spotify-downloader for downloading mp3

4. add lines for your ~/.bashrc to be able to change terminal title thru cli, see attached "add to .bashrc" file

5. ```sudo apt install util-linux```

for "script" command, output from terminal into file

6. ```pip3 install py3langid```

from https://pypi.org/project/py3langid/ detects what language is used

7. ```pip install cutlet```

from https://github.com/polm/cutlet converts jap to romaji

8. ```cargo install pinyin-tool```

from https://github.com/briankung/pinyin-tool converts chi to pinyin

9. build and install kroman

from https://github.com/victorteokw/kroman converts kor to romaja

10. ```pip3 install syrics```

from https://github.com/akashrchandran/syrics downloads lyrics from spotify
needs spotify CLIENT ID/SECRET

11. mxlrc.py from https://github.com/fashni/MxLRC already here on ./data

downloads lyrics from Musixmatch
you need to intall Musixmatch app no need for an account, run it in terminal and look for token
put the token on ./data/LyrMusixmatch

12. Netease_LRC.py from https://gist.github.com/blueset/43172f5ecd32e75d9f9bc6b7e0177755 already on ./data

downloads lyrics from Netease
      
13. put your client ID/Secret on ./Spotify downloader

14. make sure all the scripts are executable

Now all you need to do is play a song in your spotify and run in terminal ./Spotify downloader
all other description is commented in their respective script.



https://github.com/GitEin11/script-for-spotify-mp3-and-synched-lyrics-downloader/assets/84138811/33ecb6fa-0ac2-491b-a4c6-76a0d6f3d52e




