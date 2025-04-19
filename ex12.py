# faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto


preco = float(input('Qual e o preco do produto? R$'))
novo = preco - (preco * 5 / 100)

print('O preco que custava {.:2f}, na promocao com desconto de 5% vai custar R${.:2f}'.format(preco, novo))