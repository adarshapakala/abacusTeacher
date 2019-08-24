## To generate the voice from the text
from gtts import gTTS
import pygame
import time
from tkinter import *

mainWindow = Tk()
mainWindow.title("Abacus teaher")
mainWindow.geometry('500x500')
lbl1 = Label(mainWindow, text="Hello....Lets start...")
lbl1.grid(column=4, row=1)

pygame.mixer.init()
tts = gTTS(text='10', lang='en')
print("Save started ", time.ctime())
tts.save('good.mp3')
print("Save ended ", time.ctime())

pygame.mixer.music.load("good.mp3")
pygame.mixer.music.play()

mainWindow.mainloop()






