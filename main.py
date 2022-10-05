import math
import numpy as np
import matplotlib.pyplot as plt

# Ecriture d'une image
def ecrireImagePgm(name, mat, lx, ly, ng):
    f = open(name, 'w')
    s = "P2 \n#This is a PGM image\n" + str(lx) + " " + str(ly) + "\n" + str(ng) + "\n"

    for i in mat:
        for j in i:
            s += str(j) + " "
        s += "\n"
    f.write(s)
    f.close()


# Lecture d'une image
def lireImagePgm(name, dim):
    f = open(name, 'r')
    i = 0
    j = 0
    for line in f:
        i += 1
        if (i == 3):
            x, y = line.split(" ")
            dim['lx'] = int(x)
            dim['ly'] = int(y)
            mat = [[0 for _ in range(dim['ly'])]] * dim['lx']

        if (i > 4):
            mati = line.split(" ")
            mati[len(mati) - 1] = mati[len(mati) - 1].split("\n")
            mati[len(mati) - 1] = mati[len(mati) - 1][0]
            if ('' in mati):
                mati = mati.remove('')
            mat[j] = mati
            mat[j] = list(map(int, mati))
            j += 1

    f.close()
    return (mat)


# Moyenne
def moyenne(mat, dim):
    sum = 0
    for i in mat:
        for j in i:
            sum += j
    m = (1 / (dim['lx'] * dim['ly'])) * sum
    return m


# Ecart Type
def ecartType(mat, dim):
    sum = 0
    moy = moyenne(mat, dim)
    for i in mat:
        for j in i:
            sum += ((j - moy) ** 2)

    ecart = math.sqrt((1 / (dim['lx'] * dim['ly'])) * sum)
    return ecart


# histogramme
def histogramme(mat):
    h = [0] * (256)
    for i in range(0, 256):
        h[i] = 0

    for i in mat:
        for j in i:
            h[j] += 1
    return h


# histogramme cumul� :
def histogramCumule(h):
    hc = [0] * (256)
    hc[0] = 0
    for i in range(1, 256):
        for j in range(1, i + 1):
            hc[i] += h[j]
    return hc


# Test
dim = {'lx': 0, 'ly': 0}
mat = lireImagePgm("chat2.pgm", dim)
print(mat, dim)
print(dim)
print(moyenne(mat, dim))
print(ecartType(mat, dim))
h = histogramme(mat)
print(h)
print(histogramCumule(h))

# visualization de l'histogramme
plt.rcParams["figure.figsize"] = [10, 7]
plt.rcParams["figure.autolayout"] = True
plt.title("Histograme")
plt.plot(range(0, 256), h, color="red")
plt.show()

# visualization de l'histogramme cumul�
plt.rcParams["figure.figsize"] = [10, 7]
plt.rcParams["figure.autolayout"] = True
plt.title("Histograme Cumul�")
plt.plot(range(0, 256), histogramCumule(h), color="blue")
plt.show()
