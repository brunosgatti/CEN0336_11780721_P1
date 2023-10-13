#!/usr/bin/env python3

import sys
DNA = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
d = sys.argv[4]
e = sys.argv[5]
f = sys.argv[6]
g = sys.argv[7]
#Usando o import sys para poder inserir as variáveis na linha de comando


n1 = int(b)
n2 = int(c)
n3 = int(d)
n4 = int(e)
n5 = int(f)
n6 = int(g)
#Usando a função int(x) para tornar as variáveis númericas em inteiros


print(type(DNA), type(n1), type(n2), type(n3), type(n4), type(n5), type(n6))
#Conferindo os tipos de cada variável


print('\nDNA lenght is', len(DNA), '\nAll ns must be smaller than that.')

if n1 > len(DNA):
    print('n1 too big')

if n2 > len(DNA):
    print('n2 too big')

if n3 > len(DNA):
    print('n3 too big')

if n4 > len(DNA):
    print('n4 too big')

if n5 > len(DNA):
    print('n5 too big')

if n6 > len(DNA):
    print('n6 too big')
#Criando condições de tamanho para cada n, e imprimindo um aviso caso o valor atribuído a n seja maior do que o permitido com o comprimento da sequência de DNA como limitante

#Extraindo o que há entre CDS1 e CDS2
intron2 = DNA[39:46]
print('\nA sequência entre CDS1 e CDS2 é:', intron2)

if intron2.startswith('G'):
    if intron2[1] == 'T':
        if intron2[-1] == 'G':
            if intron2[-2] == 'A':
                print('A sequência entre CDS1 e CDS2 começa com os nucleotídeos GT e termina com os nucleotídeos AG')
            else:
                print('A sequência entre CDS1 e CDS2 começa com os nucleotídeos GT, mas não termina com AG, apenas com G')
        else:
            print('A sequência entre CDS1 e CDS2 começa com os nucleotídeos GT, mas não termina com os nucleotídeos AG')
    else:
        print('A sequência entre CDS1 e CDS2 começa com o nucleotídeo G, mas sem o T')
else:
    print('A sequência CDS1 e CDS2 não começa com os nucleotídeos GT')
#Com essa sequência lógica podemos determinar se a sequência segue o pedido no enunciado, mas de uma maneira mais trabalhosa, para que possamos identificar qual condição não é satisfeita, deixando as condições de início da sequência como prioritárias


#Extraindo o que há entre CDS2 e CDS3

intron3 = DNA[56:63]
print('\nA sequência entre CDS2 e CDS3 é:', intron3)
if intron3.startswith('G'):
    if intron3[1] == 'T':
        if intron3[-1] == 'G':
            if intron3[-2] == 'A':
                print('A sequência entre CDS2 e CDS3 começa com os nucleotídeos GT e termina com os nucleotídeos AG')
            else:
                print('A sequência entre CDS2 e CDS3 começa com os nucleotídeos GT, mas não termina com AG, apenas com G')
        else:
            print('A sequência entre CDS2 e CDS3 começa com os nucleotídeos GT, mas não termina com os nucleotídeos AG')
    else:
        print('A sequência entre CDS2 e CDS3 começa com o nucleotídeo G, mas sem o T')
else:
    print('A sequência CDS2 e CDS3 não começa com os nucleotídeos GT')
#Com essa sequência lógica podemos determinar se a sequência segue o pedido no enunciado, mas de uma maneira mais trabalhosa, para que possamos identificar qual condição não é satisfeita, deixando as condições de início da sequência como prioritárias

print('\n')

if intron3.startswith('GT'):
    if intron3.endswith('AG'):
        if intron2.endswith('AG'):
            if intron3.startswith('GT'):
                print(DNA[21:38], DNA[47:55], DNA[64:97], sep='')
#De uma maneira mais simplificada, testando as condições propostas no item 3 e 4, e, caso verdadeiras, concatenando os éxons.

