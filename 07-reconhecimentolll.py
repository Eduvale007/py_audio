from random import randint
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os


def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

cria_audio('dados/welcome.mp3', 'Escolha um número entre 1 a 10')

recon = sr.Recognizer()
with sr.Microphone() as source:
    print('Diga alguma coisa:')
    audio = recon.listen(source)

numero_texto = recon.recognize_google(audio, language='pt-br')

word_to_digit = {
    'um': 1,
    'dois': 2,
    'três': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'dez': 10
}

#numero_digito = word_to_digit[numero_texto]

resultado = randint(1, 10)
print(resultado)

if numero_texto == resultado:
    cria_audio('dados/venceu.mp3', 'Parabéns. Você acertou o número')
else:
    cria_audio('dados/perdeu.mp3', 'Infelizmente você errou. Tente novamente')