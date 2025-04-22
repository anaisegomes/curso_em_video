# crie um programa que leia um numero real qualquer pelo teclado e 
# mostre na tela a sua porcao inteira
# exemplo: 
# Digite o numero 6.127
# o numero 6.127 tem a parte inteira 6
#
import math
num = float(input('Digite um numero: '))
print('O numero {} tem a parte inteira {}'.format(num, math.floor(num)))