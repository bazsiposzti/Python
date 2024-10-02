Szamok = [21, 32, 13, 44, 75]
szam = int(input("Mondj egy számot:"))
melyiket = int(input("Melyik számra módosítsa?"))

index = melyiket - 1

if index >= len(Szamok)  or index < 0:
    print("nincs ilyen elem")
else:
    Szamok[index] = szam

Szamok.pop()
print(Szamok)


print(Szamok)
print(f'A meglévő listának hossza {len(Szamok)} db hosszú')

for x in Szamok:
    print(x)