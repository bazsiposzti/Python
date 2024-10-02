Számok = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Számok2 = [x for x in range(2,21)]
list(range (2,21)) 
print(Számok2)

#2. feladat
txt = "The end justifies the means"
szavak = txt.split()
print(szavak)

Fizzbuzz = [x for x in range(1,51)]
Fizzbuzz.sort(key=lambda x: x %2)
print(Fizzbuzz)