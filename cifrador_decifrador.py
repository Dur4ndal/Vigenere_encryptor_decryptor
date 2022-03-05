#!/usr/bin/python

#Cifrador/Decifrador baseado na cifra de Vigenere
#Rodrigo Mamédio Arrelaro
#190095164

import sys

key = list(input('Digite a chave\n'))
plaintext = list(input('Digite o texto plano\n'))
ciphertext = list(input('Digite a cifra\n'))

#Limpa espaços -----------> ADD função para letras em caixa alta
try:
        while True:
                plaintext.remove(' ')
                ciphertext.remove(' ')
except ValueError:
        pass

#Vetor alfabeto
base = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Cifrador
# O(n)
Index_key = 0
for C_plaintext in plaintext:

        if((base.index(C_plaintext) + base.index(key[Index_key]))>25):
                print (base[(base.index(C_plaintext) + base.index(key[Index_key])) - 26], end='')
        else:
                print (base[(base.index(C_plaintext) + base.index(key[Index_key]))], end='')
        Index_key+=1

#Arrumar essa espaguetada aqui !
Index_key=0
print ('\n')

#Decifrador
# O(n)
for C_ciphertext in ciphertext:

        if((base.index(C_ciphertext) - base.index(key[Index_key]))<0):
                print (base[(base.index(C_ciphertext) - base.index(key[Index_key])) + 26], end='')
        else:
                print (base[(base.index(C_ciphertext) - base.index(key[Index_key]))], end='')
        Index_key+=1

#Debugger
#       print ('Z {} ---- X value {} and Y value {}'.format(z,x,y))
