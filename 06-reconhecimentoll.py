import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    tts.save(audio)
    playsound(audio)
    os.remove(audio)


cria_audio('dados/welcome.mp3', 'Olá. Vou reconhecer a sua voz')

recon = sr.Recognizer()
with sr.Microphone() as source:
    print('Diga alguma coisa:')
    audio = recon.listen(source)


frase = recon.recognize_google(audio, language='pt')
cria_audio('dados/mensagem.mp3', frase)