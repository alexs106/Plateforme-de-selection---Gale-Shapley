""". Ecrivez deux m´ethodes prenant en param`etre un nombre ´ n d’´etudiants :
— l’une g´en´erant un matrice CE des pr´ef´erences de ces n ´etudiants sur les 9 parcours du master
(pr´ef´erences al´eatoires),
— l’autre g´en´erant une matrice CP des pr´ef´erences des 9 parcours du master sur les n ´etudiants
(pr´ef´erences al´eatoires)."""

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
    
    print(result)
    write(result, "PrefSpeRandom"+str(n)+".txt")


pref_spe_random(14)

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

    print(result)
    write(result, "PrefEtuRandom"+str(n)+".txt")


pref_etu_random(14)