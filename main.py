from n_class import Nevezetesség

nevezetességek = []

def inputFile(file):
    f = open(file, "r")
    for s in f:
        adat = s[:-1].split(";")
        nevezetességek.append(Nevezetesség(adat[0], adat[1], adat[2], adat[3], adat[4]))
    f.close()

inputFile("nevezetessegek.txt")

for s in nevezetességek:
    print(s.név + " - " + s.leírás)