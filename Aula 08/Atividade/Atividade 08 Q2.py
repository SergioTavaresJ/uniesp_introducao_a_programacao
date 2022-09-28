#[FORBELLONE, 2022] Construa um algoritmo que, tendo como 
#dados de entrada dois pontos quaisquer do plano,
# P(x1, y1) e Q(x2, y2), 
#imprima a distância entre eles.
#A formulá que efetua tal cálculo é: d = (x2 - x1)2 + (y2 - y1)2

from cmath import sqrt

#Inserido coordenadas dos pontos
xA = float(input('Digite o valor de ponto A: '))
xB = float(input('Digite o valor de ponta B: '))

yA = float(input('Digite o valor do ponto A:'))
yB = float(input('Digite o valor do ponto B:'))

#Calculando a Distância
distAB = sqrt(((xA-xB)**2)+((yA-yB)**2)**2)

#Mostrando resultado
print('A distância entre esses dois pontos é de:',distAB, 'unidade de medida')




