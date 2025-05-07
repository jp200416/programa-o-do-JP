#calculo da questão 2

import sys

distancia = int(input('20km'))
if distancia <=0:
    sys.exit('informe distancia positiva')
v_mi = int(input('12km/h'))
if v_ini <=0:
    sys.exit('informe velocidade positiva')
aceleração = int(imput('75m/s'))
if aceleração <=0:
    sys.exit('informe aceleração positiva')
distancia *= 1000
v_mi /=3.6
delta = v_mi**2-4*aceleração*distancia
if delta <0:
    sys.exit