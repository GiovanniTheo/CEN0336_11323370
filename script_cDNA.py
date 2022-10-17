#!/usr/bin/env python3
#Importei o módulo sys para poder usá-lo
import sys

DNA = (sys.argv[1])
x = len(DNA)
teste1 = DNA.isdigit()
if teste1:
    sys.exit("ERRO! Coloque uma sequência de DNA sem números")

n1 = (sys.argv[2])
teste2 = n1.isdigit()
if not teste2:
    sys.exit("ERRO! Coloque um número inteiro")
n1 = int(n1)
if n1 >= x:
    sys.exit("ERRO! Coloque um número inteiro menor que o tamanho da sequência de DNA")

n2 = (sys.argv[3])
teste3 = n2.isdigit()
if not teste3:
    sys.exit("ERRO! Coloque um número inteiro")
n2 = int(n2)
if n2 >= x:
    sys.exit("ERRO! Coloque um número inteiro menor que o tamanho da sequência de DNA")

n3 = (sys.argv[4])
teste4 = n3.isdigit()
if not teste4:
    sys.exit("ERRO! Coloque um número inteiro")
n3 = int(n3)
if n3 >= x:
    sys.exit("ERRO! Coloque um número inteiro menor que o tamanho da sequência de DNA")

n4 = (sys.argv[5])
teste5 = n4.isdigit()
if not teste5:
    sys.exit("ERRO! Coloque um número inteiro")
n4 = int(n4)
if n4 >= x:
    sys.exit("ERRO! Coloque um número inteiro menor que o tamanho da sequência de DNA")