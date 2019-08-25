## To generate the voice from the text
from gtts import gTTS
import pygame
import time
import tkinter as tk
import os

mainWindow = tk.Tk()
mainWindow.title("Abacus teacher")
mainWindow.geometry('500x500')

lbl1 = tk.Label(mainWindow, text="Hello....Lets start...", font=90)
lbl1.pack(fill=tk.X, padx=10, pady=50)
mainWindow.lift()
# MainWindow.attributes("-topmost", True)
pygame.mixer.init()
time.sleep(1)

d = [5, -2, 3]
s = 0


def dectate(dectNumber, lastSum, ):
    if dectNumber > 0:
        tts = gTTS(text='+' + str(dectNumber), lang='en')
    else:
        tts = gTTS(text=str(dectNumber), lang='en')
    # f = TemporaryFile()
    tts.save('good.mp3')
    pygame.mixer.music.load('good.mp3')
    pygame.mixer.music.play()
    lastSum += dectNumber
    time.sleep(1)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    os.remove('good.mp3')

    return lastSum


for i in d:
    def updateTxt():
        lbl1["text"] = str(i)


    mainWindow.after(500, updateTxt())
    mainWindow.update()
    s = dectate(i, s)
#    lbl1 = tk.Label(mainWindow, text=str(i), font=40)

mainWindow.mainloop()
