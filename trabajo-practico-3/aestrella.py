import numpy as np
import random as rm
from os import system, name 
from time import sleep
from copy import deepcopy
from math import sqrt

class Laberinto:

    def __init__(self,size,obs_rate):
        self.xSize=size
        self.ySize=size
        self.seed=rm.randrange(1000)
        self.simb=[" ","H","*","0","X"]
        self.obsQty = round(size*size*obs_rate)
        self.resetWorld()
        
    def resetWorld(self):
        rm.seed(self.seed)
        self.step=0
        self.initX = rm.randrange(self.xSize)
        self.initY = rm.randrange(self.ySize)
        
        self.xPos = self.initX
        self.yPos = self.initY
        self.finalX = rm.randrange(self.xSize)
        self.finalY = rm.randrange(self.ySize)
        self.matrix = np.zeros( (self.xSize, self.ySize) )
        self.matrix[self.finalX][self.finalY]=4
        self.matrix[self.initX][self.initY]=3
        for _ in range(self.obsQty):
            done=False
            while(not done):
                x=rm.randrange(self.xSize)
                y=rm.randrange(self.ySize)
                if(self.matrix[x][y]==0):
                    self.matrix[x][y]=1
                    done=True

    def process_action(self,action):
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
    def isObjective(self):
        if(self.xPos == self.finalX and self.yPos == self.finalY):
            return True
        return False

    def isRoad(self):
        self.matrix[self.xPos][self.yPos]=2
    
    def run_agent(self,agent):
        self.resetWorld()
        agent.init(self.initX,self.initY,self.finalX,self.finalY,self.matrix)
        while(self.step<1000):
            sleep(1)
            action=agent.think()
            self.process_action(action)
            self.step+=1
            if(self.isObjective()):
                break
            self.isRoad()
        self.print_environment()
        print("Tomó",self.step,"pasos")
        

    def print_environment(self):
        system('clear')
        for y in range(self.ySize):
            row=""
            for x in range(self.xSize):
                if(x==self.xPos and y==self.yPos):
                    row+="T"
                else:
                    row+=self.simb[round(self.matrix[x][y].item())]
            print(row)

class HeuristicaOrtogonal:
    def init(self,initX,initY,finalX,finalY,matrix):
        self.paso=0
        frontier=[(initX,initY)]
        optimos={(initX,initY):0}
        caminos={(initX,initY):[]}
        self.obj=(finalX,finalY)
        visited=[]
        while(True):
            best_score=self.score(frontier[0],self.obj,optimos[frontier[0]])
            best=0
            for n in range(1,len(frontier)):
                score=self.score(frontier[n],self.obj,optimos[frontier[n]])
                if(best_score>score):
                    best_score=score
                    best=n
            node=frontier[best]
            visited.append(node)
            if node == self.obj:
                self.elCamino=caminos[self.obj]
                return
            frontier.remove(node)
            up=(node[0],node[1]-1)
            if(up[0]>=0 and up[0]<len(matrix) and up[1]>=0 and up[1]<len(matrix[0])):
                if (up) not in visited:
                    if up in frontier:
                        if(optimos[node]+1 < optimos[up]):
                            optimos[up]=optimos[node]+1
                            caminos[up]=deepcopy(caminos[node])
                            caminos[up].append("up")
                    elif(matrix[up[0]][up[1]]!=1):
                        frontier.append(up)
                        optimos[up]=optimos[node]+1
                        caminos[up]=deepcopy(caminos[node])
                        caminos[up].append("up")
            down=(node[0],node[1]+1)
            if(down[0]>=0 and down[0]<len(matrix) and down[1]>=0 and down[1]<len(matrix)):
                if (down) not in visited:
                    if down in frontier:
                        if(optimos[node]+1 < optimos[down]):
                            optimos[down]=optimos[node]+1
                            caminos[down]=deepcopy(caminos[node])
                            caminos[down].append("down")
                    elif(matrix[down[0]][down[1]]!=1):
                        frontier.append(down)
                        optimos[down]=optimos[node]+1
                        caminos[down]=deepcopy(caminos[node])
                        caminos[down].append("down")
            right=(node[0]+1,node[1])
            if(right[0]>=0 and right[0]<len(matrix) and right[1]>=0 and right[1]<len(matrix)):
                if (right) not in visited:
                    if right in frontier:
                        if(optimos[node]+1 < optimos[right]):
                            optimos[right]=optimos[node]+1
                            caminos[right]=deepcopy(caminos[node])
                            caminos[right].append("right")
                    elif(matrix[right[0]][right[1]]!=1):
                        frontier.append(right)
                        optimos[right]=optimos[node]+1
                        caminos[right]=deepcopy(caminos[node])
                        caminos[right].append("right")
            left=(node[0]-1,node[1])
            if(left[0]>=0 and left[0]<len(matrix) and left[1]>=0 and left[1]<len(matrix)):
                if (left) not in visited:
                    if left in frontier:
                        if(optimos[node]+1 < optimos[left]):
                            optimos[left]=optimos[node]+1
                            caminos[left]=deepcopy(caminos[node])
                            caminos[left].append("left")
                    elif(matrix[left[0]][left[1]]!=1):
                        frontier.append(left)
                        optimos[left]=optimos[node]+1
                        caminos[left]=deepcopy(caminos[node])
                        caminos[left].append("left")
        print(self.elCamino)
                


    def score(self,pos,obj,cost):
        hX=pos[0]-obj[0]
        hY=pos[1]-obj[1]
        if hX<0: hX*=-1
        if hY<0: hY*=-1
        return cost+hX+hY

    def think(self): # implementa las acciones a seguir por el agente
        step=self.elCamino[self.paso]
        self.paso+=1
        return step

class HeuristicaDiagonal:      
    def init(self,initX,initY,finalX,finalY,matrix):
        self.paso=0
        frontier=[(initX,initY)]
        optimos={(initX,initY):0}
        caminos={(initX,initY):[]}
        self.obj=(finalX,finalY)
        visited=[]
        while(True):
            best_score=self.score(frontier[0],self.obj,optimos[frontier[0]])
            best=0
            for n in range(1,len(frontier)):
                score=self.score(frontier[n],self.obj,optimos[frontier[n]])
                if(best_score>score):
                    best_score=score
                    best=n
            node=frontier[best]
            visited.append(node)
            if node == self.obj:
                self.elCamino=caminos[self.obj]
                return
            frontier.remove(node)
            up=(node[0],node[1]-1)
            if(up[0]>=0 and up[0]<len(matrix) and up[1]>=0 and up[1]<len(matrix[0])):
                if (up) not in visited:
                    if up in frontier:
                        if(optimos[node]+1 < optimos[up]):
                            optimos[up]=optimos[node]+1
                            caminos[up]=deepcopy(caminos[node])
                            caminos[up].append("up")
                    elif(matrix[up[0]][up[1]]!=1):
                        frontier.append(up)
                        optimos[up]=optimos[node]+1
                        caminos[up]=deepcopy(caminos[node])
                        caminos[up].append("up")
            down=(node[0],node[1]+1)
            if(down[0]>=0 and down[0]<len(matrix) and down[1]>=0 and down[1]<len(matrix)):
                if (down) not in visited:
                    if down in frontier:
                        if(optimos[node]+1 < optimos[down]):
                            optimos[down]=optimos[node]+1
                            caminos[down]=deepcopy(caminos[node])
                            caminos[down].append("down")
                    elif(matrix[down[0]][down[1]]!=1):
                        frontier.append(down)
                        optimos[down]=optimos[node]+1
                        caminos[down]=deepcopy(caminos[node])
                        caminos[down].append("down")
            right=(node[0]+1,node[1])
            if(right[0]>=0 and right[0]<len(matrix) and right[1]>=0 and right[1]<len(matrix)):
                if (right) not in visited:
                    if right in frontier:
                        if(optimos[node]+1 < optimos[right]):
                            optimos[right]=optimos[node]+1
                            caminos[right]=deepcopy(caminos[node])
                            caminos[right].append("right")
                    elif(matrix[right[0]][right[1]]!=1):
                        frontier.append(right)
                        optimos[right]=optimos[node]+1
                        caminos[right]=deepcopy(caminos[node])
                        caminos[right].append("right")
            left=(node[0]-1,node[1])
            if(left[0]>=0 and left[0]<len(matrix) and left[1]>=0 and left[1]<len(matrix)):
                if (left) not in visited:
                    if left in frontier:
                        if(optimos[node]+1 < optimos[left]):
                            optimos[left]=optimos[node]+1
                            caminos[left]=deepcopy(caminos[node])
                            caminos[left].append("left")
                    elif(matrix[left[0]][left[1]]!=1):
                        frontier.append(left)
                        optimos[left]=optimos[node]+1
                        caminos[left]=deepcopy(caminos[node])
                        caminos[left].append("left")
                
    def score(self,pos,obj,cost):
        hX=pos[0]-obj[0]
        hY=pos[1]-obj[1]
        h=sqrt(hX**2+hY**2)
        return cost+h

    def think(self): # implementa las acciones a seguir por el agente
        step=self.elCamino[self.paso]
        self.paso+=1
        return step


ag = HeuristicaOrtogonal()
env= Laberinto(20,0.1)
env.run_agent(ag)
ag2 = HeuristicaDiagonal()
env.run_agent(ag2)