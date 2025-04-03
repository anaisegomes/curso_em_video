# conversor de moedas

# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre 
# quantos dolares ela pode comprar
# considere U$ = 1.00 = R$ 6.0572


real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 6.05
print('Com R${:.2f} voce pode comprar U${:.2f}'.format(real, dolar))
