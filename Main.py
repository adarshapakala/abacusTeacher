## To generate the voice from the text
from gtts import gTTS
import pygame
import time
pygame.mixer.init()
tts = gTTS(text='Good morning', lang='en')
print("Save started ", time.ctime())
tts.save('good.mp3')
print("Save ended ", time.ctime())

pygame.mixer.music.load("good.mp3")
pygame.mixer.music.play()
time.sleep(5)






