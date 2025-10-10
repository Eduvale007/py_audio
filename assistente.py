from random import randint
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import sys


def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    tts.save(audio)
    playsound(audio)
    os.remove(audio)


def executa_comandos(acao):
     if 'fechar assistente' in acao:
         sys.exit()


def monitora_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print('Diga alguma coisa:')
            audio = recon.listen(source)
            try:
                mensagem = recon.recognize_google(audio, language='pt-br')
                mensagem = mensagem.lower()
                print('Você disse: ', mensagem)
                executa_comandos()
                break
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
        return mensagem


def main():
    cria_audio('dados/welcome.mp3', 'Ola, sou Rita. Em que posso lhe ajudar?')
    while True:
        monitora_audio()

main()