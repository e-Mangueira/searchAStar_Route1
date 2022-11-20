class AdjacentOrderedVetor:
    def __init__(self, size):
        self.numberElements = 0
        self.adjacents = [None] * size
    
    def insert(self, adjacent):
        if self.numberElements == 0:
            self.adjacents[0] = adjacent
            self.numberElements = 1
            return
        
        position = 0
        i = 0
        while i < self.numberElements:
            if adjacent.distanceAStar > self.adjacents[position].distanceAStar:
                position += 1
            i += 1
            
        for k in range(self.numberElements, position, -1):
            self.adjacents[k] = self.adjacents[k - 1]
            
        self.adjacents[position] = adjacent
        self.numberElements += 1
        
    def getFirst(self):
        return self.adjacents[0].district
    
    def show(self):
        for i in range(0, self.numberElements):
            print('{} - {}'.format(self.adjacents[i].district.name, self.adjacents[i].distanceAStar))
            