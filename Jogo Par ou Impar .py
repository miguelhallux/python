

################BIBLIOTECAS###################

import datetime #biblioteca para usar a data
now = datetime.datetime.now() #import datetime
from random import randint


################INFO###################

print ('')
print ('Exercicio \033[31m068 \033[m  - Jogo Par ou Impar ')
print ('')
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print ('')


################ ENUNCIADO DESAFIO ###################

""" 
Faca um programa que jogue com par ou impar com o computador
O jogo só sera interrompido quando o jogador perder, mostrando o total
de vitorias consecutivas que ele conquistou durante o jogo

"""


################ CODIGO ###################


parImpar = ''
resultado = ''
contador = 0


print ('')
print ('Vamos Jogar PAR ou IMPAR ? ')
while True:
    computador = randint(1,10)
    # print(computador)

    valor = int(input('Diga um Valor: '))
    parImpar = str(input('Par ou Impar: ')).upper().strip()[0]

    soma = valor + computador

    # print(soma)


    if parImpar == 'P' and soma % 2 == 0 or parImpar == 'I' and soma % 2 != 0:
        resultado = str('VENCIDO')
    else:
        resultado = str('PERDIDO')
        print(f'Voce jogou {valor} e o computador {computador}')
        print (f'A soma foi de {soma} dai , vc ter \033[31m{resultado}\033[m ') 
        print ('')
        print ('')
        print (f'GAME OVER voce venceu {contador} vez')
        break
    contador += 1
    print(f'Voce jogou {valor} e o computador {computador}')
    print (f'A soma foi de {soma} dai , vc ter \033[32m{resultado}\033[m ') 
    print ('')
    print ('VAMOS JOGAR DE NOVO')

        
