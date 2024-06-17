from pytube import YouTube
from pathlib import Path


def FindDownloadDir():
    
    home = str(Path.home())
    home += "/Downloads"
    return home

def Download(link,location=FindDownloadDir()):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(location)
    except:
        print("An error has occurred")
    print("Download is completed successfully")