import pyttsx3
engine = pyttsx3.init()
engine.say("Hello guys, This is a text to speech",)
#engine.say("Hello, This is a text to speech")
engine.runAndwait()
engine.stop()
