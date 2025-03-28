"""
Fonctions non optimales pour la partie 1
On ne cherche pas à les utiliser pendant le projet, mais juste pour montrer
notre raissonement du départ.
"""
def detestable(liste_pref, maris):
    for elem in reversed(liste_pref):
        if elem in maris:
            return elem 
        
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
        #print("pc"+str( parcours_propr))
        #print(cap_master[current])
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
