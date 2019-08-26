import numpy as np
import random as rm
from os import system, name 
from time import sleep

class Environment:

    def __init__(self,xSize,ySize,dirt_rate):
        self.xSize=xSize
        self.ySize=ySize
        self.step=0
        self.xPos = rm.randrange(xSize)
        self.yPos = rm.randrange(ySize)
        self.simb=[".","X"]
        self.matrix = np.zeros( (xSize, ySize) )
        self.dirtQty = round(xSize*ySize*dirt_rate)
        for i in range(self.dirtQty):
            done=False
            while(not done):
                x=rm.randrange(xSize)
                y=rm.randrange(ySize)
                if(self.matrix[x][y]==0):
                    self.matrix[x][y]=1
                    done=True

    def process_action(self,action):
        print(action)
        return getattr(self, "proccess_"+action, lambda: False)()

    def process_right(self):
        print("derecha")
        if(self.xPos<(self.xSize-1)):
            self.xPos+=1
        return

    def process_left(self):
        print("izquierda")
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
        step = 0
        while(step<1000):
            action=agent.think(self.xPos,self.yPos,self.xSize,self.ySize,self.is_dirty())
            self.process_action(action)
            step+=1
            self.print_environment()
            print(step,action)
            sleep(1)


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
        if(xPos==0 and yPos == 0):
            return "right"
        elif(xPos==0):
            return "up"
        elif(xPos==xSize-1 or xPos==1):
            return "down"
        elif(yPos%2==0):
            return "right"
        else:
            return "left"


env = Environment(10,10,0.1)
env.run_agent(Aspiradora())
