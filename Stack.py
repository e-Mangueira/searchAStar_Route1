class Stack:
    def __init__(self, size):
        self.size = size
        self.districts = [None] * self.size
        self.topo = -1
        
    def empilhar(self, district):
        if not Stack.fullStack(self):
            self.topo += 1
            self.districts[self.topo] = district
        else:
            print("The stack is full")
        
    def desempilhar(self):
        if not Stack.emptyStack(self):
            temp = self.districts[self.topo]
            self.topo -= 1
            return temp
        else:
            print("The stack is empty")
            return None
    
    def getTopo(self):
        return self.districts[self.topo]
    
    def emptyStack(self):
        return (self.topo == -1)
    
    def fullStack(self):
        return (self.topo == self.size - 1)
    
from Mapa import Mapa
mapa = Mapa()
stack = Stack(5)
stack.empilhar(mapa.ufma)
stack.empilhar(mapa.dist_M)
stack.empilhar(mapa.dist_B)
stack.getTopo().name
stack.desempilhar()
stack.empilhar(mapa.hospital)
        
        
