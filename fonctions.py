def lecture_preferences_etu(fichier):
    contenu = open(fichier, "r").readlines() #lecture du fichier

    mat = [] #initialisation de la matrice

    for ligne in contenu[1: ]:
        #On prend juste les préférences
        pref = [int(x) for x in (ligne.rstrip("\n").split()[2: ])]
        mat.append(pref)

    return mat

def lecture_preferences_spe(fichier):
    contenu = open(fichier, "r").readlines() #lecture du fichier

    mat = [] #initialisation de la matrice

    for ligne in contenu[2: ]:
        #On prend juste les préférences
        pref = [int(x) for x in (ligne.rstrip("\n").split()[2: ])]
        mat.append(pref)

    return mat

def capacite(fichier):
    contenu = open(fichier, "r").readlines() #lecture du fichier
    res = [int(x) for x in (contenu[1].rstrip("\n").split()[1: ])]
    return res 

#CHECK
def detestable(liste_pref, maris):
    for elem in reversed(liste_pref):
        if elem in maris:
            return elem 

def GS_etudiants(liste_pref_etu, liste_pref_spe):
    nb_etu = len(liste_pref_etu)
    cap_master = capacite(liste_pref_spe)
    liste_etu = [i for i in range(nb_etu)]
    dico_mariages = {}
    etu_propr = {}
    for i in range (nb_etu):
        etu_propr[i] = -1
    
    while liste_etu:
        current = liste_etu[0]
        etu_propr[current] +=1
        wifey = liste_pref_etu[current][etu_propr[current]]
        if cap_master[wifey] != 0:
            if wifey in dico_mariages: 
                dico_mariages[wifey].append(current)
            else:
                dico_mariages[wifey] = [current]
            cap_master[wifey] -= 1
        else:
            #CHECK





prefetu = lecture_preferences_etu("PrefEtu.txt")
prefspe = lecture_preferences_spe("PrefSpe.txt")

print(capacite("PrefSpe.txt"))
