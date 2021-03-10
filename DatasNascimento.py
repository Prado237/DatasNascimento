'''
DESAFIO:

Escreva um algoritmo que receba a data de aniversário de duas pessoas (pessoa1 e pessoa2), sendo que a
data consiste em dia, mês e ano (três variáveis separadas). Baseando nestas datas, informe se as duas
pessoas têm a mesma idade ou, em caso negativo, informe qual é a mais velha.

'''

#1º Pessoa
n1 = (input("Nome da 1º Pessoa:"))
d1 = int (input("Dia do nascimento:"))
if d1 > 31 or d1 < 1:
    print("Dia invalido")
m1 = int (input("Mês:"))
if m1 > 12 or m1 < 1: 
    print("Mês invalido")
a1 = int (input("Ano:"))
if a1 > 2021 or a1 < 1900: 
    print("Ano invalido")
#2º Pessoa
n2 = (input("Nome da 2º pessoa:"))      
d2 = int (input("Dia do nascimento:"))
if d2 > 31 or d1 < 1:
    print("Dia invalido")
m2 = int (input("Mês:"))
if m2 > 12 or m2 < 1: 
    print("Mês invalido")
a2 = int (input("Ano:"))
if a2 > 2021 or a2 < 1900: 
    print("Ano invalido")
#Resolução
if d1 == d2 and m1 == m2 and a1 == a2:
    print ("As duas pessoas tem a mesma idade")
elif d1 < d2 or m1 < m2 or a1 < a2:
   print('\n',n1, 'é mais velho(a)!')
else:
    print('\n',n2, 'é mais velho(a)!')