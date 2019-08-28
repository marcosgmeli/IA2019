import numpy as np
import random as rm
from os import system, name 
from time import sleep

class Environment:

    def __init__(self,xSize,ySize,dirt_rate):
        self.xSize=xSize
        self.ySize=ySize
        self.seed=rm.randrange(1000)
        self.simb=[".","X"]
        self.dirtQty = round(xSize*ySize*dirt_rate)
        self.resetWorld()
        
    def resetWorld(self):
        rm.seed(self.seed)
        self.step=0
        self.xPos = rm.randrange(self.xSize)
        self.yPos = rm.randrange(self.ySize)
        self.matrix = np.zeros( (self.xSize, self.ySize) )
        for _ in range(self.dirtQty):
            done=False
            while(not done):
                x=rm.randrange(self.xSize)
                y=rm.randrange(self.ySize)
                if(self.matrix[x][y]==0):
                    self.matrix[x][y]=1
                    done=True

    def process_action(self,action):
        print(action)
        return getattr(self, "process_"+action, lambda: False)()

    def process_right(self):
        if(self.xPos<(self.xSize-1)):
            self.xPos+=1
        return

    def process_left(self):
        if(self.xPos>0):
            self.xPos-=1
        return
    def process_up(self):
        if(self.yPos>0):
            self.yPos-=1
        return
    def process_down(self):
        if(self.yPos<(self.ySize-1)):
            self.yPos+=1
        return
    def process_clean(self):
        self.matrix[self.xPos][self.yPos]= 0
        return 
    def process_idle(self):
        return 
    def is_dirty(self):
        if(self.matrix[self.xPos][self.yPos]==1):
            return True
        return False
    def print_performance(self):
        print("Performance={}".format(self.dirtQty-np.sum(self.matrix)))

    def run_agent(self,agent):
        self.resetWorld()
        while(self.step<300):
            action=agent.think(self.xPos,self.yPos,self.xSize,self.ySize,self.is_dirty())
            self.process_action(action)
            self.step+=1
            self.print_environment()
            print(self.step)
            self.print_performance()
            sleep(0.02)


    def print_environment(self):
        system('clear')
        for y in range(self.ySize):
            row=""
            for x in range(self.xSize):
                if(x==self.xPos and y==self.yPos):
                    row+="0"
                else:
                    row+=self.simb[round(self.matrix[x][y].item())]
            print(row)

class Aspiradora:           
    def think(self,xPos,yPos,xSize,ySize,dirty): # implementa las acciones a seguir por el agente
        if(dirty):
            return "clean"
        elif(xPos==0 and yPos == 0):
            return "right"
        elif(xPos==0):
            return "up"
        elif((xPos==xSize-1 and yPos%2==0 ) or (xPos==1 and yPos%2==1 and yPos<ySize-1)):
            return "down"
        elif(yPos%2==0):
            return "right"
        else:
            return "left"

class AspiradoraAleatoria:      
    estados = ["right","up","down","left"]     
    def think(self,xPos,yPos,xSize,ySize,dirty): # implementa las acciones a seguir por el agente
        if(dirty):
            return "clean"
        else:
            return self.estados[rm.randrange(4)]


env = Environment(10,10,0.1)
env.run_agent(Aspiradora())
env.run_agent(AspiradoraAleatoria())
