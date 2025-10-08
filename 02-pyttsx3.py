import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'brazil')

# 1- utilizando o input
#frase = input('Digite a frase a ser falada:\n')
#engine.say(frase)
#engine.runAndWait()

# 2 utilizando arquivos
arquivo = open('dados/frase.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
engine.say(conteudo)
engine.runAndWait()