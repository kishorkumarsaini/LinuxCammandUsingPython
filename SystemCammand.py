#!/usr/bin/python3

import speech_recognition as sr

#obtain audio from microphone
r=sr.Recognizer()

with sr.Microphone() as source:
	print("say somethings")
	audio=r.listen(source)
#recognize speech using Sphinx
	
try:
	p=r.recognize_google(audio)
	l=p.lower().replace(" ", "")
	print("think you said="+l)
	print(sr.os.system(l))
	
	
		
except sr.UnknownValueError:
	print("google speech recognition could not understand audio")
except sr.RequestError as e:
	print("google speech recognition error;{0}".format(e))