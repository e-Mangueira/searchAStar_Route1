class District:
    def __init__(self, name, hospitalDistance):
        self.name = name
        self.visited = False
        self.hospitalDistance = hospitalDistance
        self.adjacents = []
    
    def addDistrictAdjacent(self, district):
        self.adjacents.append(district)
        

## Test:
c = District("Teste", 140)
c.name
c.visited
c.hospitalDistance
