import simulatedannealing as sa 
import simulatedannealingpro as sapro 
import hillclimbing as hc
import genetico as gen

tamaños=[8,10,12,15]
for t in tamaños:
    for i in range(30):
        tupla=sapro.resolverRandom(t)
        print("sapro",i,t,tupla[0],tupla[1],tupla[2],sep=";")
for t in tamaños:
    for i in range(30):
        tupla=gen.resolverRandom(t)
        print("gen",i,t,tupla[0],tupla[1],tupla[2],sep=";")



#for t in tamaños:
#    for i in range(30):
#        tupla=hc.resolverRandom(t)
#        print("hc",i,t,tupla[0],tupla[1],tupla[2],sep=";")

for t in tamaños:
    for i in range(30):
        tupla=sa.resolverRandom(t)
        print("sa",i,t,tupla[0],tupla[1],tupla[2],sep=";")