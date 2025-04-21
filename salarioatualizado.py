# faca um algoritmo que leia um salario de um funcionario e mostre seu novo salario
# com 15% de aumento
 

salario = float(input('Qual e o salario do funcionario? '))
novo = salario * (15/100)

print('O novo salario do funcionario e de R$ {:.2f}'.format(salario + novo))


