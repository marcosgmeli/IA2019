from nreinas import reinas_amenazadas as h,imprimir_tablero as pr,reinas_aleatorio as ranrein
from copy import copy
from time import sleep,time

def hill_climb(reinas):
    actual=h(reinas)
    reina=0
    pos=reinas[0]
    temp=copy(reinas)
    temp[reina]=pos
    mejor=h(temp)
    for i in range(len(reinas)):
        for j in range(len(reinas)):
            temp=copy(reinas)
            temp[i]=j
            if(h(temp)< mejor):
                mejor=h(temp)
                reina=i
                pos=j
    reinas[reina]=pos
    return h(reinas)<actual
def resolverRandom(tamaño):
    max_estados=10000
    estado=0
    reinas=ranrein(tamaño)
    start=time()
    while(True):
        mejoro=hill_climb(reinas)
        sleep(1)
        if(not mejoro or max_estados<estado):
            #print("Tomó",estado,"pasos para llegar a una solucion con",h(reinas),"reinas amenazadas")
            demora=time()-start
            return (estado,h(reinas),demora)
        estado+=1
        
