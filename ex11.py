largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensao de {}x{} e sua area e de {}m2'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, voce precisara de {}l de tinta'.format(tinta))
