class OrderedVector:
    def __init__(self, size):
        self.numberElements = 0
        self.districts = [None] * size
    
    def insert(self, district):
        if self.numberElements == 0:
            self.districts[0] = district
            self.numberElements = 1
            return
        
        position = 0
        i = 0
        while i < self.numberElements:
            if district.hospitaldistance > self.districts[position].hospitaldistance:
                position += 1
            i += 1
            
        for k in range(self.numberElements, position, -1):
            self.districts[k] = self.districts[k - 1]
            
        self.districts[position] = district
        self.numberElements += 1
        
    def getFirst(self):
        return self.districts[0]
    
    def show(self):
        for i in range(0, self.numberElements):
            print('{} - {}'.format(self.districts[i].name, self.districts[i].hospitaldistance))
            

## Test:
from Mapa import Mapa
mapa = Mapa()
vetor = OrderedVector(5)
vetor.insert(mapa.ufma) # 61
vetor.insert(mapa.dist_A) # 52
vetor.insert(mapa.dist_J) # 12
vetor.show()
vetor.insert(mapa.dist_F) # 18
