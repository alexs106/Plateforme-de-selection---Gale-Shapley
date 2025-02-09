import heapq as h

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
        

#TAS -> vérifier 
def GS_etudiants(liste_pref_etu, liste_pref_spe,fichier):
    nb_etu = len(liste_pref_etu)
    cap_master = capacite(fichier) 
    liste_etu = [i for i in range(nb_etu)]
    dico_mariages = {}
    etu_propr = {}
    for i in range (nb_etu):
        etu_propr[i] = -1
    
    while liste_etu:
        current = liste_etu[0]
        etu_propr[current] +=1
        print(current)
        wifey = liste_pref_etu[current][etu_propr[current]]
        #print(dico_mariages)
        if cap_master[wifey] != 0: #si les masters ont encore des places
            if wifey in dico_mariages: 
                dico_mariages[wifey].append(current)
            else:
                dico_mariages[wifey] = [current]
            cap_master[wifey] -= 1
            liste_etu.remove(current)
        else:
            detest = detestable(liste_pref_spe[wifey],dico_mariages[wifey])
            if (liste_pref_spe[wifey].index(detest)>liste_pref_spe[wifey].index(current)) :
                #si l'étudiant qui propose est préféré dans la liste des masters
                inddest = dico_mariages[wifey].index(detest)
                dico_mariages[wifey][inddest] = current
                liste_etu.remove(current)
                liste_etu.insert(0, detest)
            #CHECK
    return dico_mariages


# Nouvelle version GS étudiants - Check
def GS_etudiants_nouv(liste_pref_etu, liste_pref_spe, capacite):
    nb_etu = len(liste_pref_etu)
    liste_etu = [i for i in range(nb_etu)]
    
    etu_propr = {etu: list(liste_pref_etu[etu]) for etu in range(nb_etu)}
    master_propr = {master: list(liste_pref_spe[master]) for master in range(len(liste_pref_spe))}
    dico_mariages = {}

    while liste_etu:
        current = liste_etu.pop()
        print("current:", current)
        print("etu prop:", etu_propr)
        master = int(etu_propr[current].pop(0)) #premier elem dans les preferences de current
        print("master:", master)

        if master not in dico_mariages:
            dico_mariages[master] = []
            h.heapify(dico_mariages[master])

        if capacite[master] > 0:
            capacite[master] -= 1
            h.heappush(dico_mariages[master], (master_propr[master].index(current),current))
        else:
            pref_max, etu_min = h.nlargest(1,dico_mariages[master])[0]

            index = master_propr[master].index(current)
            if index < pref_max:
                dico_mariages[master].remove((pref_max, etu_min))
                h.heapify(dico_mariages[master])
                liste_etu.append(etu_min)
                h.heappush(dico_mariages[master], (index, current))
            else:
                liste_etu.append(current)

    for master in dico_mariages:
        dico_mariages[master] = [etu for _, etu in sorted(dico_mariages[master])]

    return dico_mariages


def GS_parcours(liste_pref_etu, liste_pref_spe, fichier):
    nb_parcours = len(liste_pref_spe)
    cap_master = capacite(fichier) #Check à méditer
    liste_parcours = [i for i in range(nb_parcours)]
    dico_mariages = {}
    parcours_propr = {}

    for i in range (nb_parcours):
        parcours_propr[i] = -1
    
    while liste_parcours:
        current = liste_parcours[0]
        parcours_propr[current] += 1
        print("pc"+str( parcours_propr))
        print(cap_master[current])
        hubby = liste_pref_spe[current][parcours_propr[current]]
        #print(dico_mariages) 
        #print(parcours_propr)
        if hubby not in dico_mariages : 
              dico_mariages[hubby] = current
              cap_master[current] -= 1
        else:
            ex = dico_mariages[hubby]
            if (liste_pref_etu[hubby].index(ex) >liste_pref_etu[hubby].index(current)):#inde>
                #ex = dico_mariage[hubby]
                dico_mariages[hubby] = current
                liste_parcours.insert(1, ex)
                cap_master[ex]+=1 
                #PROBLEME
                if cap_master[current] > 0:
                    cap_master[current] -= 1
                else:
                    liste_parcours.remove(current)

        if cap_master[current] == 0:
            liste_parcours.remove(current)

    return dico_mariages

def det_paires_instables(affectXA, listeprefX, listeprefA):
    couples_instables = []

    partenaire_X = {x: a for x, a in affectXA}
    partenaire_A = {a: x for x, a in affectXA}

    for x, a in affectXA:
        pref_x = listeprefX[x]
        pref_a = listeprefA[a]

        # Trouver la position de a dans la liste de préférences de x
        pos_a = pref_x.index(a)
        # Trouver tous les a préférés
        meilleurs_a = pref_x[:pos_a]

        for a_pref in meilleurs_a:
            if a_pref in partenaire_A: 
                partenaire_actuel_x = partenaire_A[a_pref]  # Récupérer son partenaire actuel
                # Vérifier si a préfère x à son partenaire actuel
                if listeprefA[a_pref].index(x) < listeprefA[a_pref].index(partenaire_actuel_x):
                    if (x, a_pref) not in couples_instables : 
                        couples_instables.append((x, a_pref))

        #On fait la même chose du coté de x
        pos_x = pref_a.index(x)
        meilleurs_x = pref_a[:pos_x]

        for x_pref in meilleurs_x:
            if x_pref in partenaire_X:  
                partenaire_actuel_a = partenaire_X[x_pref]  
                if listeprefX[x_pref].index(a) < listeprefX[x_pref].index(partenaire_actuel_a):
                    if (x_pref, a) not in couples_instables : 
                        couples_instables.append((x_pref, a))

    return couples_instables
    
prefetu = lecture_preferences_etu("PrefEtu.txt")
prefspe = lecture_preferences_spe("PrefSpe.txt")

#print(prefetu)
#print(prefspe)
print("GS Etudiants :", GS_etudiants_nouv(prefetu, prefspe, capacite("PrefSpe.txt")))
print("GS Masters :", GS_parcours(prefetu,prefspe, "PrefSpe.txt"))
