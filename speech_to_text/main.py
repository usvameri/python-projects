import speech_recognition as sr
import pyaudio as p

r = sr.Recognizer()

# with sr.AudioFile("thespeech.wav") as source:
with sr.Microphone() as source:
    print("talk")
    audio_text = r.listen(source,timeout=5)


    try:
        # text = r.recognize_google(audio_text,None,'tr-TR')
        text = r.recognize_google(audio_text,None,'en-EN')
        print("Converting audio transcripts to text")
        print(text) 
    
    except:
        print('an error occured please try again..')