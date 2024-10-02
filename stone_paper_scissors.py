szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy másik számot: "))
Játékos1 = szam1 %3 
Játékos2 = szam2 %3
if Játékos1 == Játékos2:
    print("Döntetlen.")
elif Játékos1 == 0 and Játékos2 == 1:
    print("Játékos 2 nyert")
elif Játékos1 == 1 and Játékos2 == 2:
    print("Játékos 2 nyert")
elif Játékos1 == 1 and Játékos2 == 0:
    print("Játékos 1 nyert")
elif Játékos1 == 2 and Játékos2 == 0:
    print("Játáks 1 nyert")
elif Játékos1 == 2 and Játékos2 == 1:
    print("Játékos 1 nyert")
