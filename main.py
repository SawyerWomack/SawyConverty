#use source ./bin/activate to enable venv

#test video link: https://www.youtube.com/watch?v=C0DPdy98e4c


# from YoutubeDownload import *

# link = input("Enter the YouTube video URL: ")
# Download(link)

from VideoConversion import *

inputFilePath = input("Input the filepath wihout the extension")

Mp3ToWav(inputFilePath)

