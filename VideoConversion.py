import os
from SupportedFileTypes import *
#Uses ffmpeg to convert between video formats

def Convert(inputFile, outputFile):
    inputExtension = GetExtension(inputFile)
    outputExtension = GetExtension(outputFile)
    

    #check if input file extension is good
    if(SupportedFileTypes.count(inputExtension) == 0):
        print("input no good")
        return

    #check if output file extension is good
    if(SupportedFileTypes.count(outputExtension) == 0):
        print("output no good")
        return
    #check if they do not have the same file extension
    if(inputExtension == outputExtension):
        print("please change the output extension the the desired format")
        return

    print(inputExtension + " " + outputExtension)

    os.system("ffmpeg -i " + inputFile + " "+ outputFile+ " -hide_banner")

def GetExtension(file: str):
    length = len(file)
    index = length -1
    format = ""
    while index>0:
        if(file[index]=="."):
            return ReverseString(format)
        format += file[index]
        index -= 1

def ReverseString(String: str):
    length = len(String)
    index = length -1
    output = ""
    while index>=0:
       
        output += String[index]
        index -= 1

    return output




