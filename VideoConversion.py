import subprocess as sp
import os
import sys
from SupportedFileTypes import *
from ffmpeg_progress import start
from tkinter import messagebox

#Uses ffmpeg to convert between video formats
call = None
def ffmpeg_callback(infile: str, outfile: str, vstats_path: str):
    return sp.Popen(['ffmpeg',
                     '-nostats',
                     '-loglevel', '0',
                     '-y',
                     '-vstats_file', vstats_path,
                     '-i', infile,
                      outfile]).pid


def on_message_handler(percent: float,
                       fr_cnt: int,
                       total_frames: int,
                       elapsed: float):
    print(percent)
    call(percent)


def Convert(inputFile, outputFile,callback):
    global call
    call = callback
    inputExtension = GetExtension(inputFile)
    outputExtension = GetExtension(outputFile)

    #check if input file extension is good
    if(SupportedFileTypes.count(inputExtension) == 0):
        messagebox.showerror("Error", "Unsupported input file")
        return 1

    #check if output file extension is good
    if(SupportedFileTypes.count(outputExtension) == 0):
        messagebox.showerror("Error", "Unsupported output file")
        return
    #check if they do not have the same file extension
    if(inputExtension == outputExtension):
        messagebox.showerror("Error", "Change the output extnesion to the desired format")
        return 1 
    
    if(os.path.isfile(inputFile) == False):
        messagebox.showerror("Error", "input file does not exist")
        return 1
    
    if(os.path.isfile(outputFile) == True):
        messagebox.showerror("Error", "output file already exists")
        return 1
    
    start(inputFile,
      outputFile,
      ffmpeg_callback,
      on_message=on_message_handler,
      on_done=lambda: print('Done!'),
      wait_time=0.1)
    return 0




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
    print("start")
    Convert("/home/wiffle/Downloads/rangler.mp4", "/home/wiffle/Downloads/rangler.mp3")
    input("")
    os.remove("/home/wiffle/Downloads/rangler.mp3")