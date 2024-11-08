def feladat01_osszeg():
    szamok = [1.2, 2.3, 3.2, 4.1, 2.4, 2.3, 1.9, 0.1]
    osszeg = sum(szamok)
    return osszeg
feladat01_osszeg()

print(feladat01_osszeg())

def feladat02_osszeg():
    szamok = [1.2, -2.3, 3.2, -4.1, -2.4, 2.3, 1.9, 0.1]
    poztitiv = [szam for szam in szamok if szam > 0]
    osszeg = sum(poztitiv)

    return osszeg

print(feladat02_osszeg())

def feladat03_osszeg():
    szamok = [2, 3, 4, 9, 1, 8, 6, 1]
    paros = [szam for szam in szamok if szam %2 == 0]
    osszeg = sum(paros)

    return osszeg
print(feladat03_osszeg())

def feladat04_osszeg():
    szamok1 = [2, 3, 4, 9, 1, 8, 6, 1]
    szamok2 = [3, 1, 4, 1, 5, 4, 7, 0]
    szamok3 = []
    
    for i in range(len(szamok1)):
        if szamok1[i] > szamok2[i]:
            szamok3.append(szamok1[i])

        else:
            szamok3.append(szamok2[i])

    osszeg = sum(szamok3)
    return osszeg

print(feladat04_osszeg())

