import sys
import os 
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from SupportedFileTypes import *
from VideoConversion import Convert, test_convert
from YoutubeDownload import Download
from threading import Thread


#-------- Signal Functions-----------

#opens up the file explorer to let you select what file you want to convert
#note: there are seperate function for to and from because from automatically sets
#the to file path to the one selected
def from_open_file_dialog():
    file_name = filedialog.askopenfilename(title="Select file", filetypes=(("All files", "*.*"), ("Python files", "*.py")))
    if file_name:
        from_file_path.set(file_name)
        to_file_path.set(file_name)

#opens the file explore to select what file to turn the from file into
def to_open_file_dialog():
    file_name = filedialog.askopenfilename(title="Select file", filetypes=(("All files", "*.*"), ("Python files", "*.py")))
    if file_name:
        to_file_path.set(file_name)

#the function that gets called when the convert button gets called
def convert_file():
    #gathers the input from the user
    input_file = from_file_path.get()
    output_file = to_file_path.get()

    convert_button.config(text="Converting...")

    try:
        app.update_idletasks()
        #creates a new thread to run the convert function on
        thread = Thread(target=Convert(input_file, output_file,convert_callback))
        thread.start()
        thread.join()

        #feedback for the user (Mabey add confeti?)
        convert_button.config(text="Converted!")
        messagebox.showinfo("Success", "File converted successfully!")
    except Exception as e:
        convert_button.config(text="Convert")
        messagebox.showerror("Error", f"Conversion failed: {e}")

#a function to feed the convert progress bar with data
def convert_callback(value):
    global progress 
    progress.set(value)
    app.update_idletasks()

#function called when the download button is hit
def download_video():
    link = link_input.get()
    location = download_location.get()
    try:
        Download(link, location)
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {e}")


#-------- UI Components-----------

#a ui component that makes up all of the widgets needed to select what file you are converting
def FromBox():
    
    global from_file_path
    from_file_path = tk.StringVar()
    from_box = ttk.Frame(tab1, relief=tk.RAISED)


    label_from = ttk.Label(from_box, text='From')
    label_from.pack(side='left', padx=5)

    # Button to open file dialog
    from_file_button = ttk.Button(from_box, text="Select File", command=from_open_file_dialog)
    from_file_button.pack(side='left')

    # Textbox for file path selection
    from_file_entry = ttk.Entry(from_box, textvariable=from_file_path)
    from_file_entry.pack(side='left', fill='x', expand=True)

    from_box.pack(pady=5, fill='x')

#a ui component that makes up all of the widgets needed to select what file you are converting to
def ToBox():
    
    global to_file_path
    to_file_path = tk.StringVar()

    #container for all the components
    to_box = ttk.Frame(tab1,relief=tk.RAISED)

    #simple text
    label_to = ttk.Label(to_box, text='To')
    label_to.pack(pady=5, padx=5, side='left')

    #for the user to select in a prompt
    to_file_button = ttk.Button(to_box, text="Select File", command=to_open_file_dialog)
    to_file_button.pack(side='left')

    #to display the path as well as make it editable 
    to_file_entry = ttk.Entry(to_box, textvariable=to_file_path)
    to_file_entry.pack(side='left', fill='x', expand=True)

    to_box.pack(pady=5, fill='x')

# Create the main application window
app = tk.Tk()
app.title("File Converter")
app.geometry("600x300")

# Sets the theme of the app
style = ttk.Style(app)
app.tk.call("source", "forest-light.tcl")
style.theme_use("forest-light")



# created the tabs
notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill='both')

# ----------File Conversion Tab-----------
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="File Converter")

#adding the two frames
FromBox()

ToBox()


#button to start conversion
convert_button = ttk.Button(tab1, text="Convert", command=convert_file)
convert_button.pack(pady=5)

#bar to view progress
progress = tk.DoubleVar(app)
convert_progress = ttk.Progressbar(tab1,variable=progress)
convert_progress.pack(pady=5)

#-------- YouTube Download Tab-------------
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="YouTube Download")

# Link input
link_label = ttk.Label(tab2, text="Type link of video to download:")
link_label.pack(pady=5)

link_input = tk.StringVar()
link_entry = ttk.Entry(tab2, textvariable=link_input)
link_entry.pack(pady=5, fill='x')

# Download location input
download_label = ttk.Label(tab2, text="Where should the file download to:")
download_label.pack(pady=5)

download_location = tk.StringVar()
download_location_entry = ttk.Entry(tab2, textvariable=download_location)
download_location_entry.pack(pady=5, fill='x')

# Download button
download_button = ttk.Button(tab2, text="Download", command=download_video)
download_button.pack(pady=5)

# Run the application
app.mainloop()
