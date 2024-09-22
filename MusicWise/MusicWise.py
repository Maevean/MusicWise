#JMonize MusicWise

#importing filedialog and text from tkinter
from tkinter import *
import tkinter as tk
import pygame
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

#Before GUI pops up, choose the Root Title
print("Please Name Your Mp3 Player")
nameInp = input()
print("You chose " + nameInp)

#Initializing Pygame/ Mixer
pygame.mixer.init()


root =tk.Tk()
root.title(nameInp)
root.resizable(False,False)

#Func for Adding Song/ Removing file name and type to display only music title
def addSongs():
    chosenSong= filedialog.askopenfilename(initialdir='C:\guiPyth\Music', title="Pick a Song", filetypes=(("mp3 Files", "*.mp3"), ))
    chosenSong= chosenSong.replace("C:/guiPyth/Music/", "")
    chosenSong= chosenSong.replace(".mp3", "")
    songList.insert(END, chosenSong)

#Making Multisong Select Func
def addMultSongs():
    chosenSongs= filedialog.askopenfilenames(initialdir='C:\guiPyth\Music', title="Pick a Song", filetypes=(("mp3 Files", "*.mp3"), ))
    for chosenSong in chosenSongs:
        chosenSong= chosenSong.replace("C:/guiPyth/Music/", "")
        chosenSong= chosenSong.replace(".mp3", "")
        songList.insert(END, chosenSong)

#Playing Song
def play():
    chosenSong= songList.get(ACTIVE)
    chosenSong = f'C:/guiPyth/Music/{chosenSong}.mp3'
    pygame.mixer.music.load(chosenSong)
    pygame.mixer.music.play(loops=0)

#Global pause var
global pausing
pausing = False

#Pausing and Unpausing the song
def pause(is_pausing):
    global pausing
    pause = is_pausing
    if pausing:
        pygame.mixer.music.unpause()
        pausing=False
    else:
     pygame.mixer.music.pause()
     pausing = True

#Play Next Song in List, Getting Next Active Song, Moving Selected Song Bar
def nextSong():
    nextMusic = songList.curselection()
    nextMusic=nextMusic[0]+1
    chosenSong= songList.get(nextMusic)
    chosenSong = f'C:/guiPyth/Music/{chosenSong}.mp3'
    pygame.mixer.music.load(chosenSong)
    pygame.mixer.music.play(loops=0)
    songList.selection_clear(0, END)
    songList.activate(nextMusic)
    songList.selection_set(nextMusic, last=None)

#Previous Song in List
def prevSong():
    nextMusic = songList.curselection()
    nextMusic=nextMusic[0]-1
    chosenSong= songList.get(nextMusic)
    chosenSong = f'C:/guiPyth/Music/{chosenSong}.mp3'
    pygame.mixer.music.load(chosenSong)
    pygame.mixer.music.play(loops=0)
    songList.selection_clear(0, END)
    songList.activate(nextMusic)
    songList.selection_set(nextMusic, last=None)

#making canvas (the bg)
canvas=tk.Canvas(root, height=600, width=800, bg="#FC644C")
canvas.grid(columnspan=3, rowspan=6)
#canvas.pack()

#making the frame within the canvas
frame=tk.Frame(root, bg="black")
frame.place(relwidth=0.8, relheight=0.8, relx=0.09, rely=0.09)

#Image Info and Placement
myImg=Image.open("C:\guiPyth\MyRetro.png")
myImg=ImageTk.PhotoImage(myImg)
myImg_label=tk.Label(image=myImg)
myImg_label.image=myImg
myImg_label.grid(columnspan=3,column=0, row=2)

#Song List Box
songList = Listbox(root, bg="#FC644C", fg="white", selectbackground="black", selectforeground="#FC644C")
songList.place(relwidth=0.6, relheight=0.2, relx=0.2, rely=0.6)

#Labels
description=tk.Label(frame, text="Use Add Song to add either one or multiple songs to playlist", font="Cavolini", bg="black", fg="#FBCA70")
description.grid(columnspan=3, column=0, row=0)

#Button Images
backButtonPic = PhotoImage(file='C:\guiPyth\SkipBack.png')
fwdButtonPic = PhotoImage(file='C:\guiPyth\SkipFwd.png')
playButtonPic = PhotoImage(file='C:\guiPyth\Play.png')
pauseButtonPic = PhotoImage(file='C:\guiPyth\Pause.png')

#Buttons and their set up
backButton = Button(frame, image= backButtonPic, borderwidth=0, bg= "black", command=prevSong)
backButton.grid(column=0, row=4, columnspan=3)

fwdButton = Button(frame, image= fwdButtonPic, borderwidth=0, bg= "black", command=nextSong )
fwdButton.grid(column=3, row=4, columnspan=3)

playButton = Button(frame, image= playButtonPic, borderwidth=0, bg= "black", command=play)
playButton.grid(column=1, row=4, columnspan=3)

pauseButton = Button(frame, image= pauseButtonPic, borderwidth=0, bg= "black", command=lambda: pause(pausing))
pauseButton.grid(column=2, row=4, columnspan=3)

#Prog Menu
topMenu = Menu(root)
root.config(menu=topMenu)
#to add the songs in menu
addingSongs = Menu(topMenu)
topMenu.add_cascade(label="Add Song", menu=addingSongs)
#Adding a single song
addingSongs.add_command(label="Add a Song to Playlist", command=addSongs)
#Adding Multiple Songs
addingSongs.add_command(label="Add Multiple Songs to Playlist", command=addMultSongs)
root.mainloop()