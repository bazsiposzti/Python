# def kiiratas():
#     # name = input('Kérem a neved: ')
#     name = "Balázs"
#     print(f"A neved: {name}")

# for _ in range(4):
#     kiiratas()

# def nevkiiaratas(name):
#     print(f'Szia {name}!')

# nevkiiaratas('Kálmán')
# nevkiiaratas('Boglárka')

def terulet(szelesseg, hosszusag):
    print(f'A terület: {szelesseg * hosszusag} egység.')

# terulet(2,5)

def terfogat(a = 1, b = 2 , c = 1):
    return a * b * c

t = terfogat(1,2)
# print(f"A térfogat {t} egység")

def nevsor(*nevek):
    print(nevek)

# nevsor('Andi', 'Bea', 'Cedrik', 'Dior')

def tombkiiratas(lista):
    print(*lista, sep=' @ ')

tombkiiratas([1,1,2,3,5,8,13,21])

#min max függvény, visszatéritésben tuple

def minmax(lista):
    return (min(lista) , max(lista))

print(minmax([1,1,2,3,5,8,13,21]))

#téglatest felszíne, téglatest térfogata

def teglatest_felszin(a, b, c):
    return 2 * (a * b + a * c + b* c)
    

def teglatest_terfogata(a, b, c):
    return a * b * c

print(teglatest_felszin(1,1,1))
print(teglatest_terfogata(2,2,2))

#páros vagy páratlan szám

def paros_paratlan(number):
    result = "paros"
    if number % 2 == 1:
        result = 'paratlan'
    return result

# print(paros_paratlan(6))
# print(paros_paratlan(7))

def isEven(number):
    return number % 2 == 0

# print(isEven(6))
# print(isEven(7))

def isPrime(number):
    import math
    if number < 2: 
        return False
    result = True
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True

print(isPrime(101))