from os import system
from termcolor import colored
from random import randint

def reinas_amenazadas(reinas):
    amenazadas=0
    for i in range(len(reinas)):
        for j in range(i+1,len(reinas)):
            if(reinas[i]==reinas[j]):
                amenazadas+=1
            if(reinas[i]+(j-i)==reinas[j]):
                amenazadas+=1
            if(reinas[i]-(j-i)==reinas[j]):
                amenazadas+=1
    return amenazadas

def imprimir_tablero(reinas):
    system("clear")
    for i in range(len(reinas)):
        row=""
        for j in range(len(reinas)):
            if((i+j)%2==0):
                if(reinas[j]==i):
                    row+=colored(chr(165),"green","on_white")
                else:
                    row+=colored(" ","white","on_white")
            else:
                if(reinas[j]==i):
                    row+=colored(chr(165),"green")
                else:
                    row+=" "
                
        print(row)

def reinas_aleatorio(tamaño):
    reinas=[]
    for i in range(tamaño):
        reinas.append(randint(0,tamaño-1))
    return reinas