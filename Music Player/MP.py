from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os
import time

root=Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#171D26")
root.resizable(False,False)

mixer.init()

def play_time():
    current_time=mixer.music.get_pos()/1000
    convert_time=time.strftime('%M:%S',time.gmtime(current_time))
    status_bar.config(text=(convert_time))
    status_bar.after(1000,play_time)

#Function to play the song
def play_song():
    music_name=playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])  
    
def stop_song():
    mixer.music.stop()

def resume_song():
    mixer.music.unpause()

def pause_song():
    mixer.music.pause()

    
#Function to select the folder    
def select_folder():
    path= filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def open_lyrics_file():
    # Ask the user to select a file
    file_path = filedialog.askopenfilename()

    # Read the contents of the file
    with open(file_path, 'r') as file:
        lyrics = file.read()

    # Create a new window to display the lyrics
    lyrics_window = tk.Toplevel()
    lyrics_window.title("Lyrics")

    # Create a label to display the lyrics
    lyrics_label = tk.Label(lyrics_window, text=lyrics)
    lyrics_label.pack()

#icon
image_icon=PhotoImage(file="mp logo.png")
root.iconphoto(False,image_icon)

Top=PhotoImage(file="Top.png")
Label(root,image=Top,bg="#171D26").pack()

#logo
Logo=PhotoImage(file="music icon.png")
Button(root,image=Logo,bg="#171D26",bd=0,command=open_lyrics_file).place(x=67,y=108)

#buttons
play=PhotoImage(file="Play.png")
Button(root,image=play,bg="#171D26",bd=0,command=play_song).place(x=105,y=375)

Stop=PhotoImage(file="Stop.png")
Button(root,image=Stop,bg="#171D26",bd=0,command=stop_song).place(x=193,y=450)

Resume=PhotoImage(file="Resume.png")
Button(root,image=Resume,bg="#171D26",bd=0,command=resume_song).place(x=115,y=510)

Pause=PhotoImage(file="Pause.png")
Button(root,image=Pause,bg="#171D26",bd=0,command=pause_song).place(x=32,y=450)

#label
music=Label(root,text="",font=("times",15),fg="white",bg="#171D26")
music.place(x=150,y=340,anchor="center")

#music
Menu = PhotoImage(file="blue bg.png")
Label(root,image=Menu,bg="#171D26").pack(padx=10,pady=50,side=RIGHT)

#music Frame
music_frame= Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=330,y=350,width=560,height=250)

#select button
Button(root,text="Select Folder",width=15,height=2,font=("times",10,"bold"),fg="black",bg="#d0e8db",command=select_folder).place(x=330,y=300)



#scrollbar
scroll= Scrollbar(music_frame)
playlist= Listbox(music_frame,width=100,font=("times",15),bg="#085f6d",fg="Black",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

status_bar=Label(root,text='',fg="black",bg='#8eadbb',bd=1,relief=GROOVE,anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)
play_time()

root.mainloop()
