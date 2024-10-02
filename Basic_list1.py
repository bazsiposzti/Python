#1.feladat

erdemjegy = [1, 2, 3, 4, 5] 
osztaly = ["9/ny", "9/a", "10/b", "11/c", "12/B haladó", "1/13b", "2/14B"]
Adatok = ["Ákos", "Dénes", "Laci", "Levente", "Nelli", "Regi"]
print(erdemjegy)
print(osztaly)
print(Adatok)

#2. feladat

erdemjegy = [1, 2, 3, 4, 5] 
osztaly = ["9/ny", "9/a", "10/b", "11/c", "12/B haladó", "1/13b", "2/14B"]
Adatok = ["Ákos", "Dénes", "Laci", "Levente", "Nelli", "Regi"]

erdemjegy[0] = erdemjegy = [2]
print(erdemjegy)

osztaly[1] = osztaly[2]
print(osztaly)

# Adatok[-1] = Adatok[2]
Adatok[len(Adatok)-1] = Adatok[2]
print(Adatok)
