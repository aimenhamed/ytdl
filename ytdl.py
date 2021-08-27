import sys
import subprocess
from pytube import YouTube

if len(sys.argv) == 1:
    print("Usage: ytdl <link>")
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
        print("Trying to download: " + video)
    except:
        print("An error occurred.")
        if len(videos) == 1:
            exit(1)
        continue

    yt = yt.streams.filter(res="720p").first()
    yt.download()

    if audio == "mp3":
        print("Downloading audio: " + yt.title)
        subprocess.run(
            ["ffmpeg", "-i", f"{yt.title}.mp4", f"{yt.title}.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(
            ["rm", f"{yt.title}.mp4"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        print("Downloading video: " + yt.title)


if audio == "mp3":
    print("Successfully downloaded audio.")
elif len(videos) > 1:
    print("Successfully downloaded videos.")
else:
    print("Successfully downloaded video.")
