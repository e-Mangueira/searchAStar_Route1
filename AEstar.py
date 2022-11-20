from AdjacentOrderedVetor import AdjacentOrderedVetor

class AStar:
    def __init__(self, hospital):
        self.hospital = hospital
        self.foundHospital = False
        
    def search(self, actual):
        print('\nactual: {}'.format(actual.name))
        actual.visited = True
        
        if actual == self.hospital:
            self.foundHospital = True
        else:
            self.frontier = AdjacentOrderedVetor(len(actual.adjacents))
            for a in actual.adjacents:
                if a.district.visited == False:
                    a.district.visited = True
                    self.frontier.insert(a)
            self.frontier.show()
            if self.frontier.getFirst() != None:
                AStar.search(self, self.frontier.getFirst())
                
from Mapa import Mapa
mapa = Mapa()
aStar = AStar(mapa.hospital)
aStar.search(mapa.ufma)
