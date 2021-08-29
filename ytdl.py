import sys
import subprocess
from pytube import YouTube

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) == 1:
    print(f"{bcolors.HEADER}Usage: ytdl <link>")
    exit(1)

audio = ""

videos = sys.argv
videos.pop(0)

if videos[0] == "mp3":
    audio = videos.pop(0)

# print(videos)

for video in videos:
    try:
        yt = YouTube(video)
        print(f"{bcolors.OKGREEN}Trying to download: {bcolors.HEADER}{video}")
    except:
        print(f"{bcolors.FAIL}An error occurred.")
        if len(videos) == 1:
            exit(1)
        continue

    yt = yt.streams.filter(res="720p").first()
    yt.download()

    if audio == "mp3":
        print(f"{bcolors.OKGREEN}Downloading audio: {bcolors.HEADER}{yt.title}")
        subprocess.run(
            ["ffmpeg", "-i", f"{yt.title}.mp4", f"{yt.title}.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(
            ["rm", f"{yt.title}.mp4"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        print(f"{bcolors.OKGREEN}Downloading video: {bcolors.HEADER}{yt.title}")


if audio == "mp3":
    print("Successfully downloaded audio.")
elif len(videos) > 1:
    print("Successfully downloaded videos.")
else:
    print("Successfully downloaded video.")
