for i in range(1,51):
    kiírandó = ""
    if i %3 == 0:
     kiírandó = "Fizz"
    if i %5 == 0:
     kiírandó += "Buzz"
    if kiírandó  == "":
      kiírandó = i
    print (kiírandó, end=", ")
