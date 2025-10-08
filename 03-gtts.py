from gtts import gTTS
from playsound import playsound

tts = gTTS('Olá mundo, vamos construir nosso assistente',lang='pt-br')
tts.save('dados/audio.mp3')
playsound('dados/a')