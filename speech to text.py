# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:44:30 2020

@author: Akii
"""

import win32com.client as wincl
speak=wincl.Dispatch("SAPI.SpVoice")
import speech_recognition as sr

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('I am ready please say something')
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio=r.listen(source)
                
        Text=r.recognize_google(audio)
        
              
        print('You said-->' + Text)
        speak.Speak('You said'+ Text) 
                
                
except sr.RequestError as r:
        print('could not found audio'.format(r))
        
except sr.UnknownValueError:
        print('Error')
        
    