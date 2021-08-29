# ytdl

#### YouTube Downloader Command Line Tool

## Installation:

1. Clone the repository.
2. Install the python script dependencies `pip install requirements.txt`.
3. You can run the python script from here using `python3 ytdl.py` or you can follow the rest of the instructions to make this tool usable anywhere.
4. Run the `install.sh` bash script to install (giving executable permissions) `./install.sh`. This only works for shells with a .rc file in your ~ directory currently.
5. Source your rc file. e.g. `source ~/.bashrc`.
6. Now you can use `ytdl` anywhere :)

## Usage:

Single video download:
`ytdl {url}`

Multiple video download:
`ytdl {url1} {url2} {url3}`


## MP3 conversion integration:

With this tool you can also download a YouTube video as an MP3 file. This requires the [`ffmpeg`](https://ffmpeg.org/download.html) program which you would need to [download](https://ffmpeg.org/download.html).

#### MP3 download usage:

Single audio download:
`ytdl mp3 {url}`

Multiple audio download:
`ytdl mp3 {url1} {url2} {url3}`
