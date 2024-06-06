import os
#Uses ffmpeg to convert between video formats

os.system("echo hello")

def Mp4ToMov(inputFile):
   
    outputFile = inputFile + ".mov"
    inputFile += ".mp4"
    os.system("ffmpeg -i " + inputFile + " "+ outputFile + " -hide_banner")

def MovToMp4(inputFile):
    outputFile = inputFile + ".mp4"
    inputFile += ".mov"
    os.system("ffmpeg -i " + inputFile + " "+ outputFile + " -hide_banner")

def Mp4ToMp3(inputFile):
   
    outputFile = inputFile + ".mp3"
    inputFile += ".mp4"
    os.system("ffmpeg -i " + inputFile + " "+ outputFile + " -hide_banner")

def Mp3ToWav(inputFile):
    outputFile = inputFile + ".wav"
    inputFile += ".mp3"
    os.system("ffmpeg -i " + inputFile + " "+ outputFile + " -hide_banner")

def WavToMp3(inputFile):
    outputFile = inputFile + ".mp3"
    inputFile += ".wav"
    os.system("ffmpeg -i " + inputFile + " "+ outputFile + " -hide_banner")
