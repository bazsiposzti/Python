import random

# Hozd létre a name változót és a felhasználótól kérd be az értékét
# 2 pont

name = input("Give me your name: ")
print(name)

# Írasd ki a következő üzenetet a neme változó felhasználásával
# "Hello name felhasználó!"
# 2 pont

print(f"Hello {name} felhasználó")

# Írasd ki 5-ször egymás mellé a name változót szólözzel elválasztva!
# 2 pont

for x in name:
    print(name, end= " ")


# Kérj be egy egész és egy tizedes számot!
# 2 pont

number_int = int(input("Kérek egy egész számot: "))
number_float = float(input("Kérek egy tizedes számot: "))

print(f" Az egész szám: {number_int}")
print(f" A tizedes szám: {number_float}")

# Írd ki a két szám szorzatát!
# 2 pont

number_multiply = number_int * number_float
print(f" A két szám szorzata {number_multiply}")

# Kérj be egy hatványt, és írasd ki a tizedes szám egész hatványát!
# 2 pont

num_hatvany = int(input("Kérek egy számot: "))
hatvany_osszeg = num_hatvany ^ int(number_float)
print(f"A tizedes szám hatványa {hatvany_osszeg}")



# Döntsd el, hogy az egész szám páros vagy páratlan!
# 2 pont

if number_int % 2 == 0:
    print(f"{number_int} páros szám")

if number_int %3 == 0:
    print(f"{number_int} páratlan szám")


# Döntsd el, hogy melyik szám a nagyobb!
# 2 pont

if number_int > number_float:
    print(f"{number_int} a nagyobb szám")
else:
    number_float > number_int
    print(f"{number_float} a nagyobb szám")

# Készíts véletlen számot a két szám között!
# 2 pont

random_num = random.randrange(number_int, int(number_float))
print(f"A véletlen szám {random_num}")

# Kerekítsd egészre a tizedes számot!
# 2 pont

number_float_egesz = int(number_float)
print(f"Az egész szám: {number_float_egesz}")


# Írd ki a kerekített szám szorzótábláját 1-től 10-ig!
# 2 pont

for x in range (1, 11):
    szorzat_oszeg = x * number_float_egesz
    print(f"A kettes szorzó tábla: {x} * {number_float_egesz} = {szorzat_oszeg}")

# Add össze a lista elemeit (két megoldás)!
num_list = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
# 1. megoldás
print(f" A lista lemeinek összege: {sum(num_list)}")
# 2 pont

# 2. megoldás ciklussal

összeg = 0
for x in num_list:
    összeg += x
print(f"A lista elemeinek összege ciklussal {összeg}")
# 2 pont




# Találd meg a legkisebb és a legnagyobb elemet (két megoldás)!
# 1. megoldás
# 2 pont

num_list.sort()
print(f" A legkisebb szám: {num_list[0]}")
print(f" A legnagyobb szám: {num_list[-1]}")

# 2. megoldás ciklussal


# 2 pont


# Rendezd a lista másolatát növekvő sorrendbe!
# 2 pont

num_list_copy = num_list.copy()
num_list_copy.sort()
print(f"A lista növekvő sorrendben {num_list_copy}")


# Írasd ki a rendezett lista középső 6 elemét!
# 2 pont

print(len(num_list_copy))
print(f" A lista középső 6 eleme {num_list_copy[4:10]}")

# Készíts a lista nem egyedi elemeiből egy tuple-t!
# 2 pont

num_list = set(num_list_copy)

print(f" A tuple: {tuple(num_list)}")


# Készíts a listából egy set-et!
# 2 pont
num_list = set(num_list_copy)
print(f"A set: {num_list}")

# Készíts egy listát, amely kételemű tuple-t tartalmaz (elem, darabszám)!
# 2 pont
