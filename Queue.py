class Queue:
    def __init__(self, size):
        self.size = size
        self.districts = [None] * self.size
        self.start = 0
        self.stop = -1
        self.numberElements = 0
        
    def enfileirar(self, district):
        if not Queue.fullQueue(self):
            if self.stop == self.size - 1:
                self.stop = -1
            self.stop += 1
            self.districts[self.stop] = district
            self.numberElements += 1
        else:
            print("The queue is full")
        
    def desenfileirar(self):
        if not Queue.emptyQueue(self):
            temp = self.districts[self.start]
            self.start += 1
            if self.start == self.size:
                self.start = 0
            self.numberElements -= 1
            return temp
        else:
            print("The queue is empty")
            return None
    
    def getFirst(self):
        return self.districts[self.start]
    
    def emptyQueue(self):
        return self.numberElements == 0
    
    def fullQueue(self):
        return self.numberElements == self.size
    
from Mapa import Mapa
mapa = Mapa()
queue = Queue(5)
queue.enfileirar(mapa.canoinhas)
queue.enfileirar(mapa.dist_D)
queue.enfileirar(mapa.dist_J)
queue.getFirst().name
queue.desenfileirar()
queue.enfileirar(mapa.ufma)
            