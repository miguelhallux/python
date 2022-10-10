
################BIBLIOTECAS###################

import datetime #biblioteca para usar a data
now = datetime.datetime.now() #import datetime



################INFO###################
print ('' *40)
print ('' *40)
print ('=' *40)
print ('Exercicio \033[31m045\033[m  - PEDRA, PAPEL  E TESOURA ')
print ('=' *40)
print (now.strftime("          %Y-%m-%d %H:%M:%S"))
print ('=' *40)
print ('' *40)


################ ENUNCIADO DESAFIO ###################

""" 
Crie um programa que faca o computador jogar 
Jokenpo com vc:

"""


################ CODIGO ###################

from random import randint
from time import sleep

lista = ('PEDRA', 'TESOURA', 'PAPEL' )
print ('''
[0] Para Pedra
[1] Para Tesoura
[2] Para Papel

''')
computador = randint(0,2)


escolha = int(input('Qual a sua escolha?: '))

print ('' *40)
sleep (1)
print('PEDRA')
sleep (1)
print('PAPEL')
sleep (1)
print('TESOURA')
print ('' *40)

print (f'Voce escolheu {lista[escolha]}')
print (f'O computador escolheu {lista[computador]}')


if computador == 0 : #escolheu pedra
    if escolha == 0:
        print('Voce Empatou')
    elif escolha == 1:
        print('Voce Perdeu')
    elif escolha == 2:
        print('Voce Ganhou')
    else:
        print('Resposta INVALIDA, TENTE de novo')  

elif computador == 1: #escolheu tesoura
    if escolha == 0:
        print('Voce Ganhou')
    elif escolha == 1:
       print('Voce Empatou')
    elif escolha == 2:
        print('Voce Perdeu')
    else:
        print('Resposta INVALIDA, TENTE de novo')  
elif computador == 2:
    if escolha == 0:
        print('Voce Perdeu')
    elif escolha == 1:
       print('Voce Ganhou')
    elif escolha == 2:
        print('Voce Empatou')
    else:
        print('Resposta INVALIDA, TENTE de novo')  



