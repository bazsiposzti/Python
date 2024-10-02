Gyümölcsök = ['Alma', 'Banán', 'Cseresznye', 'Dinnye', 'Eper', 'Füge', 'Gránátálma']

print(Gyümölcsök[0],Gyümölcsök[2])
print(Gyümölcsök[:5])
print(Gyümölcsök[-5:])
print(Gyümölcsök[1:6])

Gyümölcsök[0] = 'Körte'
print(Gyümölcsök)

for x in Gyümölcsök:  #elemek felhasználásra
    print(x, end=' - ')
print()

for i in range(len(Gyümölcsök) -1):
    print(Gyümölcsök[i], end=' * ') #elemek felhasználására és változtatni
print(Gyümölcsök[-1])

Gyümi = 'füge'
if Gyümi in Gyümölcsök:
    print(F'A(z) {Gyümi} benne van a gyümölcsök listában')
else:
    print(F'A(z) {Gyümi} nincs benne van a gyümölcsök listában')

Gyümölcsök[1:3] = ['Ananász', 'Mangó', 'Kiwi']
print(Gyümölcsök)

Gyümölcsök[-3:-1] = ['Szilva']
print(Gyümölcsök)

Gyümölcsök.insert(2, 'Licsi')
print(Gyümölcsök)

Zöldségek =  ['Répa', 'retek', 'Mogyoróhagyma']

Zöldségek.append('Káposzta')
print(Zöldségek)

#Zöldségek.extend(Gyümölcsök)
saláta = Zöldségek + Gyümölcsök
print(saláta)

Zöldségek[-2:]= []
print(Zöldségek)

Zöldségek.remove('retek')
print(Zöldségek)

számaim = [2, 4, 6, 8, 12]
számaim.remove(4)
print(számaim)

számaim.pop(0)
számaim.pop()
print(számaim)

#mindegyik gyümölcs nagybetűvel kezdődjön
#for i in range(len(Gyümölcsök)):
    #Gyümölcsök[i] = Gyümölcsök[i].capitalize()
    #print(Gyümölcsök)

összeg = 0
for x in Gyümölcsök:
    összeg += len(x) 
print(f'A lista elemeinek össz hossza: {összeg}') #lista elemeinek hossza

newlist = [x for x in range(10)]

print(newlist)
lst = list(range(0,10, 2 ))
print(lst)

számok = [12, 2, 50, 34, 89, 11, 1, 28, 70, 3, 23, 3]
#számok.sort()
#számok.sort(reverse=True)
#számok.reverse()
számok.sort(key=lambda x: abs(25 - x))
print(számok)

nevek = ['Alma','bimbó', 'cica', 'Dávid', 'Eperke', 'frici']
# nevek.sort(key=lambda x: x.lower())
nevek.sort(key=str.lower)
print(nevek)

lst1 = [1, 3, 5, 7]
# lst2 = lst1.copy() 
# lst2 = lst1[:]
lst2 = list(lst1)
lst1.append(9)
print(lst1, lst2)
print(számok.count(3))
print(számok.count(23))
print(nevek.count('Eperke'))

print(számok.index(3))
print(számok.index(23))
print(nevek.index('Eperke'))

txt = 'Képzeld, nyertem a lottón,... kettesem volt'
# szavak = txt.split() #szavanként
# szavak = txt.split(' .') #megadott karakter alapján
szavak = list(txt) #karakterenként
print(szavak)

fruit = ' * '.join(Gyümölcsök)
print(fruit)