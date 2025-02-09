import random
from random import shuffle

def write(str_content, output_file):

    file = open(output_file, "w")
    file.write(str_content)
    file.close()


def pref_spe_random(n):
    result = "NbEtu "+str(n)+"\n"
    cap = [1 for i in range(9)]

    matpref = [[i for i in range(n)] for _ in range (9)]

    if n>9 :
        for i in range(n-9):
            ind = random.randint(0, 8)
            cap[ind] += 1

    for elem in matpref:
        shuffle(elem)

    result += "Cap "
    for elem in cap:
        result += str(elem)+" " 
    result +="\n"

    masters = ["ANDOIDE", "BIM", "DAC", "IMA", "RES", "SAR", "SESI", "SFPN", "STL"]

    for i in range(9):
        result += str(i) + "   "+ str(masters[i])+"   "
        for elem in matpref[i]:
            result += str(elem)+"   "
        result+= "\n"

    write(result, "PrefSpeRandom.txt")


def pref_etu_random(n):
    result = str(n)+"\n"

    matpref = [[i for i in range(9)]for _ in range(n)]

    for elem in matpref:
        shuffle(elem)

    for i in range(n):
        result += str(i) + "   "+ "Etu"+str(i)+"   "
        for elem in matpref[i]:
            result += str(elem)+ "   "
        result += "\n"

    write(result, "PrefEtuRandom.txt")


"""
TESTS DE GÉNÉRATION DES MATRICES ALÉATOIRES -> on peut remplacer les chiffres 
"""

#print(pref_etu_random(10))
#print(pref_etu_random(50))
#print(pref_spe_random(10))
#print(pref_spe_random(50))