from calendar import c
from re import I
from random import choice   

jogadores = ['will', 'morph', 'gui', 'edu', 'gg', 'dd']
times = ['Aguia', 'Macacos', 'Morcegos', 'jacares']
print('Participantes:')
print(jogadores)

nometimeA = []
nometimeB = []
nometimeC = []
timeA = []
timeB = []
timeC = []

while len(jogadores) > 0:
    jogadorA = choice(jogadores)
    timeA.append(jogadorA)
    jogadores.remove(jogadorA)

    if jogadores == []:
        break

    jogadorB = choice(jogadores)
    timeB.append(jogadorB)
    jogadores.remove(jogadorB)

    if jogadores == []:
        break

    jogadorC = choice(jogadores)
    timeC.append(jogadorC)
    jogadores.remove(jogadorC)


nomesotimeA = choice(times)
nometimeA.append(nomesotimeA)
times.remove(nomesotimeA)

nomesotimeB = choice(times)
nometimeB.append(nomesotimeB)
times.remove(nomesotimeB)

nomesotimeC = choice(times)
nometimeC.append(nomesotimeC)
times.remove(nomesotimeC)

print('Times:')
print(nometimeA, timeA)
print(nometimeB, timeB)
print(nometimeC, timeC)