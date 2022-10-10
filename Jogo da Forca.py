################BIBLIOTECAS###################

import datetime #biblioteca para usar a data
now = datetime.datetime.now() #import datetime
import random

################INFO###################
print ('' *40)
print ('' *40)
print ('=' *40)
print ('    \033[31mJogo da Forca\033[m  by Miguel Hallux ')
print ('=' *40)
print (now.strftime("          %Y-%m-%d %H:%M:%S"))
print ('=' *40)
print ('          Tem \033[31msete\033[m tentativas ')
print ('=' *40)

################ ENUNCIADO DESAFIO ###################

""" 
Fazer o jogo da forca, com 7 tentativas!!

"""
################ BONECO ###################

forca = """
________
        |
        |
        - """

vazio = """
        


"""

cabeca = """
        O
"""

tronco = """
        O
        |
"""

braço_esquerdo = """
        O
       /|
"""

braço_direito = """
        O
       /|\\
"""

perna_esquerda = """
        O
       /|\\
       /
"""

perna_direita = """
        O
       /|\\
       / \\
"""


################ LISTAS ###################

palavras = ['macaco','gato','leao','pato','cavalo', 'hipopotamo']

chances = [
vazio, 
cabeca, 
tronco,
braço_esquerdo,
braço_direito,
perna_esquerda,
perna_direita,]


""" with open ('Python/txt/palavras_forca.txt') as arquivo:
    linhas = arquivo.read()
    print(linhas) """

""" #fazer uma lista com um TXT

palavras = linhas.split()

print(palavras)
 """

################ VARIAVEIS ###################

palavra = random.choice(palavras).upper()
acertou = 0
errou = 0
letras_acertadas = ''
letras_erradas =''



################ CODIGO ###################

while acertou != len(palavra) and errou != 7:
    
    mensagem = ''
    
    
    for letra in palavra: #percorre a string com a quantidade de letras que a palavra tem
        
        if letra in letras_acertadas:
            mensagem = mensagem + letra + ' '
        else:
            mensagem += '_ '
    print(' ')
    print(mensagem)
    print(' ')

    letra = str(input('Escreva uma letra :  ')).upper()
    
    print(forca + chances[errou])
    
    if letra in letras_acertadas + letras_erradas:
        print('\033[33mJá digitaste essa letra\033[m' )
        continue
    
    if letra in palavra:
        print(f'\033[32mACERTASTE \033[mna letra, continua!!')

        letras_acertadas = letras_acertadas + letra #vai mandar para dentro da variavel as letras que foram acertadas
        acertou += palavra.count(letra) #neste caso qd ha 2 letras iguais ele vai contar como se tivesse acertado as 2 e nao 1
    else:
        print(f'\033[31mERRASTE\033[m na letra, tens mais {6 - errou} tentativa')
        letras_erradas = letras_erradas + letra #vai mandar para dentro da variavel as letras que foram acertadas
        errou += 1 #contador para o acertou

################ CODIGO FINAL ###################

if errou == 7:
    print(' ')
    print (' Voce foi \033[31mENFORCADO\033[m ')
    
else:
    print(' ')
    print (f'Voce \033[32mGANHOU\033[m ', end=',')

print (f'A palavra tem {len(palavra)} letras e voce acertou {acertou} vezes e errou {errou} vezes ')    

