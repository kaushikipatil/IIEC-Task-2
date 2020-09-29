import speech_recognition as sr
import webbrowser as wb
import pyttsx3
print()
print("Here is the Program which launch or stop Docker for You")
print()
pyttsx3.speak("Hello I am Your Docker Assistant")
print("Hello I am Your Docker Assistant")
pyttsx3.speak("I am here to help you to launch or stop your docker container")
print("I am here to help you to launch or stop your docker container")
pyttsx3.speak("Tell me your requirement") 
print("Tell me your requirement")
r=sr.Recognizer()
with sr.Microphone() as source:
 print("Listening.... ")
 audio=r.listen(source)
 print("Done....")
text=r.recognize_google(audio)
print(text)

if ("run" in text) or ("launch" in text) or ("execute" in text) and ("docker" in text) or ("container" in text):
     wb.open("http://192.168.0.106/index.html")
     pyttsx3.speak("Opening a Page launch Docker")
elif ("stop" in text) and ("docker" in text) or ("container" in text):
     wb.open("http://192.168.43.106/StopTheContainer.html")
     pyttsx3.speak("Opening a Page to Stop Docker")
else:
    print("Please Try Again")