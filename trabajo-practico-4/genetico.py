from nreinas import reinas_amenazadas as h,imprimir_tablero as pr,reinas_aleatorio as ranrein
from copy import copy
from random import randint,random
from time import sleep,time
from math import exp,ceil,floor
from prqueue import PrQueue
REINAS=8
POB_SIZE=200
SURV=0.5
MUT=True
MIX=True
def poblacion_inicial(tamaño_pob,tamaño):
    poblacion=PrQueue(h)
    for _ in range(tamaño_pob):
        poblacion.add(ranrein(tamaño))
    return poblacion

def next_gen(pob):
    size=pob.size()
    new_gen=PrQueue(h)
    for _ in range(ceil(size*SURV)):
        new_gen.add(pob.pop())
    for _ in range(floor(size*(1.0-SURV))):
        randa,randb=new_gen.getRandPair()
        new_gen.add(mix(randa,randb))
    return new_gen

def mix(a,b):
    for _ in range(len(a)//3):
        i=randint(0,len(a)-1)
        temp=copy(a)
        temp[i]=b[i]
    if(MUT):
        temp[randint(0,len(temp))-1]=randint(0,len(temp)-1)
    return temp

def resolverRandom(tamaño):
    max_gen=1000
    gen=0
    start=time()
    pob=poblacion_inicial(POB_SIZE,tamaño)
    while(True):
        #print(pob)
        #print("-",pob.qPerPr())
        if(max_gen < gen or pob.contains(0)):
            demora=time()-start
            reinas=pob.pop()
            #print("Tomó",gen,"generaciones para llegar a una solucion con",h(reinas),"reinas amenazadas")
            return (gen,h(reinas),demora)
        pob=next_gen(pob)
        gen+=1

