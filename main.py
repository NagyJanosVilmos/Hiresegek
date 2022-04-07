import os
from n_class import Nevezetesség

nevezetességek = []

def inputFile(file):
    f = open(file, "r")
    for s in f:
        adat = s[:-1].split(";")
        nevezetességek.append(Nevezetesség(adat[0], adat[1], adat[2], adat[3], adat[4]))
    f.close()

inputFile("nevezetessegek.txt")

def f1():
    for s in range(len(nevezetességek)):
        print(str(s+1) + " - " + nevezetességek[s].név)
    valasztas = int(input("Válassz egy nevezetességet amiről szeretnél többet tudni (1-" + str(len(nevezetességek)) + ")): "))
    while valasztas < 1 or valasztas > len(nevezetességek):
        valasztas = int(input("Válassz egy nevezetességet amiről szeretnél többet tudni (1-" + str(len(nevezetességek)) + ")): "))
    print("\n\n")
    v = nevezetességek[valasztas-1]
    print(v.név, "\n")
    print("Helyszín:", v.hely)
    print("Keletkezés dátuma:", v.dátum)
    print("Egyéb tudnivalók:\n")
    l = open(v.leírás, "r", encoding="utf-8", errors="ignore")
    for s in l:
        print(s, "\n")
    os.system(v.kép)

def f2():
    datum = int(input("Adj meg egy dátumot ahonnan nevezetességekről szeretnél olvasni: "))
    helyin = []

    for i in nevezetességek:
        if i.dátum == datum:
            helyin.append(i)

    print("\n")

    for s in range(len(helyin)):
        print(str(s+1) + " - " + helyin[s].név)

    if len(helyin) == 0:
        print("Nincs egy darab nevezetesség sem a megadott korban")
        return

    valasztas = int(input("Válassz egy nevezetességet amiről szeretnél többet tudni (1-" + str(len(helyin)) + ")): "))
    while valasztas < 1 or valasztas > len(helyin):
        valasztas = int(input("Válassz egy nevezetességet amiről szeretnél többet tudni (1-" + str(len(helyin)) + ")): "))
    print("\n\n")
    v = helyin[valasztas-1]
    print(v.név, "\n")
    print("Helyszín:", v.hely)
    print("Keletkezés dátuma:", v.dátum)
    print("Egyéb tudnivalók:\n")
    l = open(v.leírás, "r", encoding="utf-8", errors="ignore")
    for s in l:
        print(s, "\n")
    os.system(v.kép)

def f3():
    orszag = str(input("Adj meg egy országot ahonnan nevezetességekről szeretnél olvasni: "))
    helyin = []

    for i in nevezetességek:
        print(i.hely, "-", orszag)
        if i.hely == orszag:
            helyin.append(i)

    print("\n")

    for s in range(len(helyin)):
        print(str(s+1) + " - " + helyin[s].név)

    if len(helyin) == 0:
        print("Nincs egy darab nevezetesség sem a megadott országban")
        return

    valasztas = int(input("Válassz egy nevezetességet amiről szeretnél többet tudni (1-" + str(len(helyin)) + ")): "))
    while valasztas < 1 or valasztas > len(helyin):
        valasztas = int(input("Válassz egy nevezetességet amiről szeretnél többet tudni (1-" + str(len(helyin)) + ")): "))
    print("\n\n")
    v = helyin[valasztas-1]
    print(v.név, "\n")
    print("Helyszín:", v.hely)
    print("Keletkezés dátuma:", v.dátum)
    print("Egyéb tudnivalók:\n")
    l = open(v.leírás, "r", encoding="utf-8", errors="ignore")
    for s in l:
        print(s, "\n")
    os.system(v.kép)

f1()
f2()
f3()