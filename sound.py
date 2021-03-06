#!/usr/bin/python
from led import led
import RPi.GPIO as GPIO
import time
import requests
import subprocess
from gtts import gTTS
from pygame import mixer

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

mixer.init()
tts = gTTS(text="Namastey. Give a clap to invoke Gecho", lang='en')
tts.save("good.mp3")
mixer.music.load('./good.mp3')
mixer.music.play()
while mixer.music.get_busy() == True:
	continue


def subroutine():
	res = requests.get("http://e5b95c82.ngrok.io/testImage")
	print res.content
	led(res.content)

def my_func():
	result = requests.get("http://a7250838.ngrok.io/invoke")
	print result.content
	return subroutine

def callback(channel):
	print "Give a clap to invoke"
	if not GPIO.input(channel):
		subroutine = my_func()
		subroutine()

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
	time.sleep(1)
