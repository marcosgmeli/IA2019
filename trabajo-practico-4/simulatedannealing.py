from nreinas import reinas_amenazadas as h,imprimir_tablero as pr,reinas_aleatorio as ranrein
from copy import copy
from random import randint,random
from time import sleep,time
from math import exp

def prob(delta,estado):
    return exp(delta/-(1/(0.001*(estado+1))))
def next_step(reinas,estado):
    actual=h(reinas)
    reina=randint(0,len(reinas)-1)
    pos=randint(0,len(reinas)-1)
    temp=copy(reinas)
    temp[reina]=pos
    nuevo=h(temp)
    delta=nuevo-actual
    if(delta<=0):
        reinas[reina]=pos
        return
    if(prob(delta,estado)>=random()):           
        #print(prob(delta,estado),delta,estado,delta/(estado+1))
        reinas[reina]=pos
def resolverRandom(tamaño):
    max_estados=10000
    estado=0
    reinas=ranrein(tamaño)
    start=time()
    while(True):
        next_step(reinas,estado)
        
        if(max_estados<estado or  h(reinas)==0):
            #print("Tomó",estado,"pasos para llegar a una solucion con",h(reinas),"reinas amenazadas")
            demora=time()-start
            return (estado,h(reinas),demora)
        estado+=1
