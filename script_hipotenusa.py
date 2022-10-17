#!/usr/bin/env python3
#Importei os módulos sys e math para poder usá-los
import sys
import math
#armazeinei os valores que o usuário irá fornecer em variáveis e testei para ver se é ou não número inteiros, caso não fossem uma mensagem de erro aparece
a = (sys.argv[1])
teste1 = a.isdigit()
if not teste1:
        sys.exit("ERRO! Coloque um número inteiro")
a = int(a)
#coloquei a variável em int para poder testar se é menor que 500 e rodar na equação montada
if a >= 500:
        sys.exit("ERRO! Coloque um número inteiro menor que 500")
#uma mensagem de erro aparece se o número for maior ou igual a 500
b = (sys.argv[2])
#repeti os testes para a variável b
teste2 = b.isdigit()
if not teste2:
        sys.exit("ERRO! Coloque um número inteiro")
b = int(b)
if b >= 500:
        sys.exit("ERRO! Coloque um número inteiro menor que 500")
z = math.sqrt(a*a + b*b)
#montei a equação utiliando o math e coloquei uma mansagem de resposta se tudo estiver certo
print("O quadrado da hipotenusa para o triangulo retângulo com lados a=",a, "e b=",b, "é",z)