from gtts import gTTS
from playsound import playsound
import os

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    tts.save('dados/mensagem.mp3')
    playsound('dados/mensagem.mp3')
    os.remove('dados/mensagem.mp3')


 #1-usando diretamente
cria_audio('Aprendendo a criar um assistente virtual') 


 #2-usando com input
frase = input('Digite a frase a ser falada:\n')
cria_audio(frase)


#3-usando com arquivo

arquivo = open("dados/frase.txt", 'r', encoding='utf-8')
conteudo = arquivo.read()
cria_audio(conteudo)