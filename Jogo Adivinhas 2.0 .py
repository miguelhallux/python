



################BIBLIOTECAS###################

import datetime #biblioteca para usar a data
now = datetime.datetime.now() #import datetime



################INFO###################
print ('' *40)
print ('' *40)
print ('=' *40)
print ('Exercicio \033[31m057\033[m  - Validação de Dados')
print ('=' *40)
print (now.strftime("          %Y-%m-%d %H:%M:%S")) 
print ('=' *40)
print ('' *40)


################ ENUNCIADO DESAFIO ###################

""" 

Faca um programa que faca o computador pensar
em um numero inteiro entre 0 e 10 e peça para o usuario
tentar descobrir qual foi o numero escolhido
pelo computador

O programa devera escrever na tela se o usuario venceu ou perdeu
Mostra no fim quantos palpites foram necessarios para vencer

"""



################ CODIGO ###################

from random import randint

numero = randint(0,11)
contador = 0

while numero < 10:
    adivinha = int(input('Digite um numero de 0 a 10: '))
    if adivinha == numero:
        print ('ACERTOU')
        break
    else:
        if adivinha > numero:
            print (f'Tente de novo, o numero escolhido pelo computador é MENOR ')
        else:
            print (f'Tente de novo, o numero escolhido pelo computador é MAIOR ')
    contador += 1 

print(f'o numero escolhido pelo mac foi {numero} o numero de tentativas FALHADAS foi de {contador}')




