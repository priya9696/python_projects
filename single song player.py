from tkinter import *
import pygame#3rd party module
from pygame import mixer

root = Tk()
root.title('MP3Playe.com')
root.geometry("500x400")

 #initializing pygame
pygame.mixer.init()

#functions
def play():
      #pygame.mixer.music.load("D:/ProgramFiles/roa-music-summer-madness.MP3")
      pygame.mixer.music.load("D:/ProgramFiles/roa-music-summer-madness.MP3")
      pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

#Buttons

my_button=Button(root, text="Play song", font=("Helvetica", 32), command = play)
my_button.pack(pady=20)

stop_button= Button(root, text="Stop", command = stop)
stop_button.pack(pady=20)
 
root.mainloop()
#you always end your script by calling the mainloop method of the root window.
#When that method returns, your program will exit.
