from tkinter import filedialog, Text, Scrollbar
from tkinter import *
from tkinter import messagebox
import customtkinter as cusTK
import pyktok as py
from TikTokApi import TikTokApi

cusTK.set_appearance_mode("dark") 
cusTK.set_default_color_theme("blue")

# Initialize app
app = cusTK.CTk()
app.title('Tik Tok Download Version 1.0')
# app.iconbitmap('icon/icon.ico')
app.geometry('400x460')
app.resizable(0,0)

# Function to browse files
def browFiles():
    file_path = filedialog.askopenfilename(title="Select a File", 
                                           filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    if file_path:
        entry.delete(0, END)
        entry.insert(0, file_path)

# Function to download TikTok videos
def downloadVideos():
    file_path = entry.get()
    if not file_path:
        append_message("No file selected.")
        return
    
    try:
        # Read video URLs from the selected file
        with open(file_path, 'r') as file:
            myvideos = file.read().strip().splitlines()  # Split by lines for multiple URLs
        
        # Specify the browser for pyktok
        py.specify_browser('chrome')

        # Loop through each URL in the file
        for video_url in myvideos:
            # Save the TikTok video
            append_message(f"Saving video from: {video_url}")
            py.save_tiktok(video_url, True)
            append_message(f"Completed: {video_url}")
        messagebox.showinfo("Complete","Your Videos Download Complete!")
        append_message("Download complete.")
    
    except FileNotFoundError:
        append_message("The selected file was not found.")
    except Exception as e:
        append_message(f"An error occurred: {e}")
    
    # Clear entry field after download
    entry.delete(0, END)

# Function to append messages to the scrollable frame
def append_message(message):
    text_widget.insert(END, message + "\n")
    text_widget.yview(END)  # Auto-scroll to the end

# Label
label = cusTK.CTkLabel(app, text="Tool Download Video From TikTok", fg_color="transparent", 
                       font=("Comic Sans MS", 17), text_color="dark gray")
label.place(x=60, y=10)

# Entry
entry = cusTK.CTkEntry(app, placeholder_text="Enter your part list URL", width=200)
entry.place(x=60, y=80)

# Button to browse files
button = cusTK.CTkButton(app, text="Browse Files", width=50, command=browFiles)
button.place(x=280, y=80)

# Button to download videos
buttonDown = cusTK.CTkButton(app, text="Download", width=87, command=downloadVideos)
buttonDown.place(x=280, y=120)

# Scrollable frame
scrollable_frame = cusTK.CTkScrollableFrame(app, width=330, height=200, border_color='light blue', scrollbar_fg_color='light pink',border_width=2)
scrollable_frame.place(x=30, y=200)

# Text widget for displaying messages
text_widget = Text(scrollable_frame, wrap=WORD, height=10, width=36)
text_widget.pack(side=LEFT, fill=BOTH, expand=True)

# Scrollbar
scrollbar = Scrollbar(scrollable_frame, command=text_widget.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_widget.config(yscrollcommand=scrollbar.set)

copyright_label = cusTK.CTkLabel(app, text="© 2024 Damrith Som. All rights reserved.", font=("Arial", 10))
copyright_label.pack(side="bottom", pady=10, anchor="e")

# Start app loop
app.mainloop()
