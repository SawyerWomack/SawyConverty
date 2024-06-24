from pytube import YouTube
from pytube.cli import on_progress
import pytube.request
from pathlib import Path

pytube.request.default_range_size = 1000

def FindDownloadDir():
    
    home = str(Path.home())
    home += "/Downloads"
    return home

def Download(link,location=FindDownloadDir(),progress_function=None):
    if location=="":
        location=FindDownloadDir()
    print("going")
    youtubeObject = YouTube(link, on_progress_callback=progress_function)

    global video
    video = youtubeObject.streams.first()
    
    video.download(location)
    print("Download is completed successfully")

#def progress_function(stream, chunk, bytes_remaining):
#    print(round((1-bytes_remaining/video.filesize)*100, 3), '% done...')

def test_download():
    Download("https://www.youtube.com/watch?v=C0DPdy98e4c")
    Download("https://www.youtube.com/watch?v=zBnDWSvaQ1I")


