import pyttsx3
engine = pyttsx3.init()
engine.say("this is a python that what you was telling ")
robi = input("enter word ")
engine.say(robi)
engine.runAndWait()
