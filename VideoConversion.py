import subprocess
import os
from SupportedFileTypes import *
from UIModules import ErrorMessage
#Uses ffmpeg to convert between video formats

def Convert(inputFile, outputFile):

    inputExtension = GetExtension(inputFile)
    outputExtension = GetExtension(outputFile)

    inputFile = inputFile
    #inputFile = "\'" + inputFile+"\'"
    #outputFile = "\'" + outputFile+"\'"

    outputFile = outputFile
    
    
    
    #check if input file extension is good
    if(SupportedFileTypes.count(inputExtension) == 0):
        ErrorMessage("Input file extension is not supported")
        return

    #check if output file extension is good
    if(SupportedFileTypes.count(outputExtension) == 0):
        print("output no good")
        return
    #check if they do not have the same file extension
    if(inputExtension == outputExtension):
        ErrorMessage("please change the output extension the the desired format")
        return
    
    if(os.path.isfile(inputFile) == False):
        ErrorMessage("input file does not exist")
        return
    
    if(os.path.isfile(outputFile) == True):
        ErrorMessage("output file already exists")
        return
    
    #check if the input file is a video

    command = [
        
        "ffmpeg",
        "-i",
        inputFile,
        outputFile,
        "-hide_banner"
    ]
    
    print("going")

    process = subprocess.Popen(command,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.wait()
    print(return_code)
    if return_code == 0:
        print(stderr.decode())
        stdout, stderr = process.communicate( input=b"y\n")
        return_code = process.wait()
        
    print(return_code)


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



#write a test for the convert function
def test_convert():
    Convert("/home/wiffle/Downloads/rangler.mp4", "/home/wiffle/Downloads/rangler.mp3")


test_convert()