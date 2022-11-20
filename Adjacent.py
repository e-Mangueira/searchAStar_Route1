class Adjacent:
    def __init__(self, district, distance):
        self.district = district
        self.distance = distance
        self.distanceAStar = self.district.hospitalDistance + self.distance
        