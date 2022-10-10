def ini_matriz(tamanho):
   # O unico propósito dessa funcao e iniciar uma matriz
   m = [[0 for g in range (tamanho[1])] for i in range(tamanho[0])]
   return m
def mostra_matriz(matriz):
   # essa funcao serve pra printar a matriz
   for i in matriz:
       print(i)
def jogada(matriz,coluna,token):
   #essa funcao coloca a jogada na matriz
   for i in range(len(matriz)-1,-1,-1):
       token , matriz[i][coluna] = matriz[i][coluna], token
   return matriz
def verificar(jogo):
   # essa funcao verifica se há ganhadores
   for i in range(len(jogo)):
       cont = [0,0] #Matriz para contar quantas pecas tem na horizontal
       for j in range(len(jogo[i])):
           if cont[1] >= 4:
               return cont[0]
           elif jogo[i][j]:
               if cont[0] ==jogo[i][j]:
                   cont[1]+=1
               else:
                   cont[0] = jogo[i][j]
                   cont[1] = 1
           else:
               cont = [0,0]
   for i in range(len(jogo[1])):
       cont = [0,0] #Matriz para contar quantas pecas tem na vertical
       for j in range(len(jogo)):
           if jogo[j][i]:
               if cont[0] ==jogo[j][i]:
                   cont[1]+=1
               else:
                   cont[0] = jogo[j][i]
                   cont[1] = 1
           else:
               cont = [0,0]
           if cont[1] >= 4:
               return cont[0]
         
           
   for i in range(4-1,len(jogo)):
       for g in range(len(jogo[1])-(4-1)):
           cont = [0,0] # matriz para contar quantas pecas tem na diagonal
           for k in range(4):
               if jogo[i-k][g+k]:
                   if cont[0] ==jogo[i-k][g+k]:
                       cont[1]+=1
                   else:
                       cont[0] = jogo[i-k][g+k]
                       cont[1] = 1
               else:
                   break
           if cont[1] >= 4:
               return cont[0]
   for i in range(len(jogo)-(4-1)):
       for g in range(len(jogo[1])-(4-1)):
           cont = [0,0] # matriz para contar quantas pecas tem na diagonal
           for k in range(4):
               if jogo[i+k][g+k]:
                   if cont[0] ==jogo[i+k][g+k]:
                       cont[1]+=1
                   else:
                       cont[0] = jogo[i+k][g+k]
                       cont[1] = 1
               else:
                   break
           if cont[1] >= 4:
               return cont[0]
   return 0
           
def main():
   tamanho = (6,7) #serve pra setar o tamanho do jogo
   jogo = ini_matriz(tamanho)
   ganhou = 0 # serve pra parar o jogo quando alguem ganhar
   jogador = 0 # serve pra saber quem vai jogar
   while not ganhou:
       mostra_matriz(jogo)
       print('Quem vai jogar é o jogador ', jogador%2 +1,'.')
       print('Escolha em qual coluna você quer jogar (escolha de 1 a ',tamanho[1],'): ')
       escolha = int(input())
       while escolha<1 or escolha>tamanho[1]:
               print('Número inválido.')
               print('Escolha em qual coluna você quer jogar (escolha de 1 a ',tamanho[1],'): ')
               escolha = int(input())
       jogo = jogada(jogo,escolha-1, jogador%2 +1)
       ganhou = verificar(jogo)
       jogador +=1
               
   mostra_matriz(jogo)
   print('O jogador', ganhou,' venceu!!')
   return 0
if __name__ == "__main__":
   main()
