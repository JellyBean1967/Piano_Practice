# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
import time
import subprocess

# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'

def remindWithVoice(mytext, phaseName):
    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save(phaseName + ".mp3")

    # Playing the converted file
    subprocess.Popen("ffplay " + phaseName + ".mp3")

secondsInMin=60
mytext="Welcome to piano practice. First we have to play scales for 15 mins"
remindWithVoice(mytext, "scales")
time.sleep(15*secondsInMin)
print(mytext)

mytext="Time up! Time for Czerny! This will take 15 minutes."
remindWithVoice(mytext, "Czerny")
time.sleep(15*secondsInMin)
print(mytext)

mytext="Bach is going to take over for 20 min!"
remindWithVoice(mytext, "Bach")
time.sleep(20*secondsInMin)
print(mytext)

mytext="Now Mozart is marching up the hall, you will play his piece for 40 minutes."
remindWithVoice(mytext, "Mozart Concerto")
time.sleep(40*secondsInMin)
print(mytext)

mytext="I think I saw Chopin in the living room, will you play for him?"
remindWithVoice(mytext, "Chopin Nocturne and Etude")
time.sleep(60*secondsInMin)
print(mytext)
