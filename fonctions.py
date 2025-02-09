import heapq as h

#Lecture des préférences des étudiants
def lecture_preferences_etu(fichier):
    contenu = open(fichier, "r").readlines() #lecture du fichier

    mat = [] #initialisation de la matrice

    for ligne in contenu[1: ]:
        #On prend juste les préférences
        pref = [int(x) for x in (ligne.rstrip("\n").split()[2: ])]
        mat.append(pref)

    return mat

#Lecture des préférences des parcours
def lecture_preferences_spe(fichier):
    contenu = open(fichier, "r").readlines() #lecture du fichier

    mat = [] #initialisation de la matrice

    for ligne in contenu[2: ]:
        #On prend juste les préférences
        pref = [int(x) for x in (ligne.rstrip("\n").split()[2: ])]
        mat.append(pref)

    return mat

#Lecture de la capacité des parcours
def capacite(fichier):
    contenu = open(fichier, "r").readlines() #lecture du fichier
    res = [int(x) for x in (contenu[1].rstrip("\n").split()[1: ])]
    return res 


"""
Fonction qui prend une liste de préférence côté étudiants et parcours, 
ainsi que la capacité des parcours afin d'appliquer l'algorithme de 
Gale-Shapley côté étudiants

Retourne : Un dictionnaire des couples formés
"""
def GS_etudiants_nouv(liste_pref_etu, liste_pref_spe, capacite):
    nb_etu = len(liste_pref_etu)
    liste_etu = [i for i in range(nb_etu)]
    
    etu_propr = {etu: list(liste_pref_etu[etu]) for etu in range(nb_etu)} # dico etu - liste pref etu
    master_propr = {master: list(liste_pref_spe[master]) for master in range(len(liste_pref_spe))} # dico master - liste pref spe
    dico_mariages = {}

    #tant qu'il y a un etudiant libre
    while liste_etu:
        current = liste_etu.pop()
        master = int(etu_propr[current].pop(0)) #premier elem dans les preferences de current

        if master not in dico_mariages:
            dico_mariages[master] = []
            h.heapify(dico_mariages[master])

        #si le master n'a pas atteint sa capacité 
        if capacite[master] > 0:
            capacite[master] -= 1
            h.heappush(dico_mariages[master], (master_propr[master].index(current),current))
        else: #si on a atteint la capacité max
            pref_max, etu_min = h.nlargest(1,dico_mariages[master])[0]

            index = master_propr[master].index(current)
            if index < pref_max: #si on préfère un autre étudiant
                dico_mariages[master].remove((pref_max, etu_min)) # on enlève l'étudiant min
                h.heapify(dico_mariages[master])
                liste_etu.append(etu_min) #on remets l'étudiant min dans les étudiants libres
                h.heappush(dico_mariages[master], (index, current))
            else:
                liste_etu.append(current) #sinon, on rejète la proposition de current

    #On change le tas en une liste
    for master in dico_mariages:
        dico_mariages[master] = [etu for _, etu in sorted(dico_mariages[master])]

    #On retourne le dictionnaire avec des couples
    return dico_mariages

"""
Fonction qui prend une liste de préférence côté étudiants et parcours, 
ainsi que la capacité des parcours afin d'appliquer l'algorithme de 
Gale-Shapley côté parcours

Retourne : Un dictionnaire des couples formés
"""
def GS_parcours_nouv(liste_pref_etu, liste_pref_spe,capacite):
    nb_masters = len(liste_pref_spe)
    liste_masters = [i for i in range(nb_masters)]

    etu_propr = {etu: list(liste_pref_etu[etu]) for etu in range(len(liste_pref_etu))} # dico etu - liste pref etu
    master_propr = {master: list(liste_pref_spe[master]) for master in range(nb_masters)} # dico master - liste pref spe
    dico_mariages = {}
    parcours = {master: [] for master in range(nb_masters)}

    #tant qu'il y a un master libre
    while liste_masters:
        master = liste_masters.pop()

        while capacite[master] > 0:
            etudiant = int(master_propr[master].pop(0))

            #Si l'étudiant est libre, on les mets en couple et on diminue la capacité du amster
            if etudiant not in dico_mariages:
                dico_mariages[etudiant] = master
                capacite[master] -= 1
                h.heappush(parcours[master], (etu_propr[etudiant].index(master), etudiant))

            else:
                current = dico_mariages[etudiant]
                index_current = etu_propr[etudiant].index(current) #index du parcours affecté à current
                index_master = etu_propr[etudiant].index(master)

                if index_current > index_master: #si 'master' est mieux classé que le master affecté

                    liste_masters.append(current)
                    capacite[current] += 1
                    dico_mariages[etudiant] = master
                    capacite[master] -= 1
                    h.heappush(parcours[master], (index_master, etudiant))
                    #on enlève l'étudiant du parcours actuel
                    parcours[current] = [(mast, etu) for mast, etu in parcours[current] if etu != etudiant]
                    h.heapify(parcours[current])
    
    for m in parcours:
        parcours[m] = [etu for _, etu in sorted(parcours[m])]

    return dico_mariages

"""
Fonctions qui vérifie si on a des paires instables dans nos résultats de Gale-Shapley
"""
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


"""
TEST POUR LES FONCTIONS GALE-SHAPLEY
"""

#print(prefetu)
#print(prefspe)
#print("GS Etudiants :", GS_etudiants_nouv(prefetu, prefspe, capacite("PrefSpe.txt")))
#print("GS Masters :", GS_parcours_nouv(prefetu,prefspe, capacite("PrefSpe.txt")))

#print(det_paires_instables([(1,5),(0,6),(7,7),(3,0),(4,1),(10,4),(9,2),(5,0),(6,8),(2,8),(8,3)], prefetu, prefspe))
#print(det_paires_instables([(6,1),(2,9),(5,0),(7,7),(4,10),(0,5),(0,3),(1,4),(8,6),(8,2),(3,8)], prefspe, prefetu))

