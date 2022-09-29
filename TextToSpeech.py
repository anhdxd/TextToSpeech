#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyttsx3
import os
import io


engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("volume",1)
    
listfiles = os.listdir('TDNVC')
for file in listfiles:
    text=""
    filename = file
    with io.open("TDNVC\\"+filename,'r',encoding='utf8') as f:
        text = f.read()
    #engine.say(text)
    engine.save_to_file(text,filename.replace(".txt",".wav"))
    engine.runAndWait()

