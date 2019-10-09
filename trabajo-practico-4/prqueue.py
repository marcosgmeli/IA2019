from random import choice
from copy import copy

class PrQueue(object): 
    def __init__(self,priority): 
        self.queue = {}
        self.priority=priority
  
    def __str__(self): 
        return str(self.queue)
  
    def isEmpty(self): 
        return len(self.queue) == [] 
  
    def add(self, data):
        pr=self.priority(data)
        if(not pr in self.queue):
            self.queue[pr]=[]
        self.queue[pr].append(data)

        
    def pop(self): 
        i=0
        for _ in range(len(self.queue)):
            while(True):
                if(i in self.queue):
                    break
                i+=1
            if(len(self.queue[i])>0):
                val=self.queue[i].pop()
                if(len(self.queue[i])==0):
                    self.queue.pop(i)
                return val
            i+=1
    
    def qPerPr(self):
        return {k:len(v) for (k,v) in self.queue.items()}

    def size(self):
        size=0
        for val in self.queue.values():
            size+=len(val)
        return size
    
    def getRandPair(self):
        l=choice(list(self.queue.values()))
        a=choice(l)
        m=choice(list(self.queue.values()))
        b=choice(m)
        while(a==b):
            m=choice(list(self.queue.values()))
            b=choice(m)
        return (a,b)
    
    def contains(self,i):
        return i in self.queue
