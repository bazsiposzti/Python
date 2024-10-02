nap_sorszáma = int(input('Add meg napnak a sorszámát: '))

match nap_sorszáma:
      case 0 | 1 | 2 | 3 | 4: print("Munkanap") 
      case 5 | 6: print("Hétvége")
      case _: print("Rossz napot adtál meg")