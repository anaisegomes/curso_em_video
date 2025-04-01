medida = float(input('Uma distancia em metros: '))

dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida /1000

print('A medida de {}m corresponde a \n{}cm e \n{}mm, \n{}dm \n{}dam \n{}hm \n{}km'.format(medida, cm, mm, dm, dam, hm, km))
