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

d = [2, 1, 2]
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
    lbl1["text"] = str(i)
    mainWindow.update()
    s = dectate(i, s)

lbl1["text"] = 'And answer is:'
tts = gTTS(text='And your answer is', lang='en')
tts.save('good.mp3')
time.sleep(1)
pygame.mixer.music.load('good.mp3')
pygame.mixer.music.play()
time.sleep(4)
pygame.mixer.music.stop()
pygame.mixer.music.unload()
os.remove('good.mp3')
lbl1["text"] = 'And answer is:' + str(s)
mainWindow.update()
mainWindow.mainloop()
