a = input('Digite algo: ')
print('O tipo primitivo desse valor e', type(a))
print('So tem espacos?', a.isspace())
print("E um numero? ", a.isnumeric())
print('E alfabetico?', a.isalpha())
print('E alfanumerico?', a.isalnum())
print('Esta em maiusculas', a.isupper()) # maiuscula
print('Esta em minusculas', a.islower()) # minuscula
print('Esta capitalizada', a.istitle())