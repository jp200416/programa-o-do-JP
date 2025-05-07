#calculo da questão 2

import sys

distancia = int(input('20km'))
if distancia <=0:
    sys.exit('informe distancia positiva')
v_mi = int(input('12km/h'))
if v_mi <=0:
    sys.exit('informe velocidade positiva')
aceleração = int(input('75m/s'))
if aceleração <=0:
    sys.exit('informe aceleração positiva')
distancia *= 1000
v_mi /=3.6
delta = v_mi**2-4*aceleração*distancia
if delta <0:
    sys.exit('não é possivel calcular o tempo')

tempo = (-v_mi+delta**0.5)/(2*aceleração)