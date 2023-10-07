#!/usr/bin/env python3

import sys #Importando os valores
a = sys.argv[1] #Determinando o índice da variável a
b = sys.argv[2] #Determinando o índice da variável b
A = (int(a)*int(b))/2 #Determinando a fórmula da área de um triângulo
#print(a.isdigit())
#print(b.isdigit())

if a.isdigit(): #Determinando se o valor de a é um inteiro
    print('')
else:
    print('O valor inserido para a não é um inteiro')

if b.isdigit(): #Determinando se o valor de b é um inteiro
    print('')
else:
    print('O valor inserido para b não é um inteiro')

print('A área do triângulo retãngulo com lados a=X e b=Y, é ', A) #Imprimindo o resultado da fórmula com os valores atribuídos na linha de comando, bem como adicionando uma frase para complementar a resposta



#Podemos fazer usando o comando input, ao invés do import sys, como vemos abaixo
#print(input('Entre um valor para a: '))
#print(input('Entre um valor para b: '))
#A = (int(a)*int(b))/2
#print('A área do triângulo retângulo com lados a=X e b=Y, é ', A)

