from District import District
from Adjacent import Adjacent

class Mapa:
    ufma = District("UFMA", 61)
    dist_A = District("District A", 52)
    dist_B = District("District B", 42)
    dist_D = District("District D", 41)
    dist_F = District("District F", 18)
    dist_M = District("District M", 8)
    hospital = District("Hospital", 0)
    dist_J = District("District J", 12)
    dist_K = District("District K", 6)
    dist_N = District("District N", 4)
    dist_I = District("District I", 11)
    dist_H = District("District H", 28)
    dist_L = District("District L", 16)
    dist_G = District("District G", 22)
    dist_C = District("District C", 37)
    dist_E = District("District E", 39)
    
    ## Adjacency among the districts
    
    ufma.addDistrictAdjacent(Adjacent(dist_A, 13))  
    ufma.addDistrictAdjacent(Adjacent(dist_B, 24))
    ufma.addDistrictAdjacent(Adjacent(dist_C, 26))
       
    dist_A.addDistrictAdjacent(Adjacent(ufma, 13))
    dist_A.addDistrictAdjacent(Adjacent(dist_D, 22))
    
    dist_B.addDistrictAdjacent(Adjacent(ufma, 24))
    dist_B.addDistrictAdjacent(Adjacent(dist_E, 4))
    dist_B.addDistrictAdjacent(Adjacent(dist_H, 20))
    
    dist_D.addDistrictAdjacent(Adjacent(dist_A, 22))
    dist_D.addDistrictAdjacent(Adjacent(dist_F, 22))
    dist_D.addDistrictAdjacent(Adjacent(dist_C, 17))
    
    dist_F.addDistrictAdjacent(Adjacent(dist_D, 22))
    dist_F.addDistrictAdjacent(Adjacent(dist_C, 23))
    dist_F.addDistrictAdjacent(Adjacent(dist_M, 16))
    
    dist_M.addDistrictAdjacent(Adjacent(dist_F, 16))
    dist_M.addDistrictAdjacent(Adjacent(dist_J, 7))
    dist_M.addDistrictAdjacent(Adjacent(hospital, 9))
    
    hospital.addDistrictAdjacent(Adjacent(dist_M, 9))
    hospital.addDistrictAdjacent(Adjacent(dist_J, 15))
    hospital.addDistrictAdjacent(Adjacent(dist_K, 13))
    hospital.addDistrictAdjacent(Adjacent(dist_N, 5))
    
    dist_J.addDistrictAdjacent(Adjacent(hospital, 15))
    dist_J.addDistrictAdjacent(Adjacent(dist_M, 7))
    dist_J.addDistrictAdjacent(Adjacent(dist_I, 6))
    
    dist_K.addDistrictAdjacent(Adjacent(hospital, 13))
    dist_K.addDistrictAdjacent(Adjacent(dist_I, 5))
    
    dist_N.addDistrictAdjacent(Adjacent(hospital, 5))
    dist_N.addDistrictAdjacent(Adjacent(dist_L, 15))
    
    dist_I.addDistrictAdjacent(Adjacent(dist_J, 6))
    dist_I.addDistrictAdjacent(Adjacent(dist_K, 5))
    dist_I.addDistrictAdjacent(Adjacent(dist_G, 8))

    dist_H.addDistrictAdjacent(Adjacent(dist_L, 30))
    dist_H.addDistrictAdjacent(Adjacent(dist_G, 17))
    dist_H.addDistrictAdjacent(Adjacent(dist_B, 20))
    
    dist_L.addDistrictAdjacent(Adjacent(dist_H, 30))
    dist_L.addDistrictAdjacent(Adjacent(dist_N, 15))

    dist_G.addDistrictAdjacent(Adjacent(dist_I, 8))
    dist_G.addDistrictAdjacent(Adjacent(dist_C, 18))
    dist_G.addDistrictAdjacent(Adjacent(dist_H, 17))
    
    dist_C.addDistrictAdjacent(Adjacent(dist_F, 23))
    dist_C.addDistrictAdjacent(Adjacent(dist_D, 17))
    dist_C.addDistrictAdjacent(Adjacent(dist_G, 18))
    dist_C.addDistrictAdjacent(Adjacent(dist_E, 13))
    dist_C.addDistrictAdjacent(Adjacent(ufma, 26))
    
    dist_E.addDistrictAdjacent(Adjacent(dist_C, 13))
    dist_E.addDistrictAdjacent(Adjacent(dist_B, 4))
    
mapa = Mapa()
mapa.ufma.name
mapa.ufma.visited
mapa.ufma.adjacents
mapa.ufma.hospitalDistance
for i in range(len(mapa.ufma.adjacents)):
    print(mapa.ufma.adjacents[i].district.name)
