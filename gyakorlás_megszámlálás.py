def feladat01() -> int:
    jegyek = [2, 5, 4, 5, 3, 3, 5, 5, 4, 5, 2, 3, 5, 5, 5, 3]
    otosok = []

    for i in range (len(jegyek)):
        if jegyek[i] == 5:
            otosok.append(jegyek[i])
    
    return len(otosok)

print(feladat01())

def feladat02() -> int:
    jegyek = [2, 5, 4, 1, 3, 3, 5, 1, 4, 5, 1, 3, 1, 5, 5, 3]
    atment_tantargyak = []
    
    for i in range (len(jegyek)):
        if jegyek[i] != 1:
            atment_tantargyak.append(jegyek[i])
    
    return len(atment_tantargyak)

print(feladat02())

def feladat03() -> int:
    szamok = [-21, 15, 4, -1, 3, -3, 51, 11, -41, 51, 8, 31, -11, 9, -4, 9, -2, -10]
    egyjegyu = []
    
    for i in range (len(szamok)):
        if szamok[i] <= 10 and szamok[i] > -10 :
            egyjegyu.append(szamok[i])
    
    return len(egyjegyu)

print(feladat03())

def feladat04() -> int:
    szamok = [-21, 15, 4, -1, 3, -3, 51, 11, -41, 51, 8, 31, -11, 9, -4, 9, -2, -10, -1, -32, 65, 42]
    ketjegyu = []
    
    for i in range (len(szamok)):
        if szamok[i] >= 10:
            ketjegyu.append(szamok[i])
        elif szamok[i] <= -10:
            ketjegyu.append(szamok[i])
    
    return len(ketjegyu)

print(feladat04())

    
