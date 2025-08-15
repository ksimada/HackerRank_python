# FizzBuzz
# Dado um número n, para cada inteiro i no intervalo de 1 a n inclusive, imprima um valor por linha da seguinte forma:
# Se i for múltiplo de 3 e 5, imprima FizzBuzz.
# Se i for múltiplo de 3 (mas não de 5), imprima Fizz.
# Se i for múltiplo de 5 (mas não de 3), imprima Buzz.
# Se i não for múltiplo de 3 ou 5, imprima o valor de i.

# Descrição da Função
# Complete a função fizzBuzz no editor abaixo.
# fizzBuzz tem o(s) seguinte(s) parâmetro(s):
# int n: limite superior dos valores a serem testados (inclusive)
# Retorna: NADA
# Imprime:
# A função deve imprimir a resposta apropriada para cada valor 
# i
# i no conjunto 
# {
# 1
# ,
# 2
# ,
# .
# .
# .
# ,
# n
# }
# {1,2,...,n} em ordem crescente, cada uma em uma linha separada.

# Restrições
# 0 <n<2×10**5
# 0<n<2×10**5
 
# Formato de Entrada para Testes Personalizados
# A entrada do stdin será processada da seguinte forma e passada para a função.
# O único inteiro n, o limite do intervalo a ser testado: 
# [
# 1
# ,
# 2
# ,
# .
# .
# .
# ,
# n
# ]
# [1,2,...,n].
# ________________________________________________________________

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for i in range (1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        elif i % 3 != 0 and i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)