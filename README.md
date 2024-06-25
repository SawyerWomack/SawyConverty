# SawyConverty
This tool has one philosephy: Ease of use
I created this tool to avoid those horrible websites that make you download malware whenever you want to convert from mp4 to mov and also to avoid the complex tools that give far too much information when all i  want to do is convert from mp4 to mov. 
This tool solves both of these problems by creating a simple and intewitive way to download youtube videos and convert between different media file types

# Installation
If you are on  a debian based system, simply download the .deb file and install it using
```
sudo dpkg -i SawyConverty.deb
```


While I work on creating a windows installer, this is how you download and run the program
First make sure you have all of the python packages that are listed below

Probably already installed:
- subprocess
- os
- threading

Use pip to install:
- Tkinter
- SupportedFileTypes
- ffmpeg_progress
- pytube
- pathlib

After this, download the src file and extract it. After that simply run main.py and youre good to go!

# How To Use
Most of the use is pretty intuitive but I will describe anyway.

## youtube download
Say you wanted to download a youtube video with this url:https://www.youtube.com/watch?v=HInd4QQrgKI

The first step would be to click on the tab at the top of the window that sats youtube download. Then select a download location. Note that if you leave that part blank, it will try to guess where your download folder is.
After that just click the download button and wait for it to download

## File Conversion
Say you wanted to convert that video that is on you desktop.
You would click on the button next to the from label and select the file, for example "/home/user/Desktop/video.mp4"
it will automagically but this path into the to input box where you simply change the extension the the format you want to use. Finally just hit the convert button and wait
