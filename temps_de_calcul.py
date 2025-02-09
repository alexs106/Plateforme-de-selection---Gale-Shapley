import time
import matrices_aleatoires as mat
import fonctions as f
import matplotlib.pyplot as plt

def temps_calcul_GS_etudiant(liste_n, liste_temps):
    n = 200

    while n<=2000:
        #Tests 10 par n
        for i in range(10): 
            sum_etu = 0

            #Définition des données
            mat.pref_etu_random(n)
            mat.pref_spe_random(n)
            
            prefetu = f.lecture_preferences_etu("PrefEtuRandom.txt")
            prefspe = f.lecture_preferences_spe("PrefSpeRandom.txt")

            #GS côté étudiants
            start = time.time()
            f.GS_etudiants_nouv(prefetu, prefspe, f.capacite("PrefSpeRandom.txt"))
            end = time.time()

            print("GS Etudiants Time " + str(end-start))
            sum_etu += end-start

        avg_etu = sum_etu/10

        print("------------------------------")

        liste_n.append(n)
        liste_temps.append(avg_etu)
        n+= 200

        
def temps_calcul_GS_master(liste_n, liste_temps):
        n = 200

        while n<=2000:
            for i in range(10):
                sum_master = 0

                mat.pref_spe_random(n)
                mat.pref_etu_random(n)

                prefetu = f.lecture_preferences_etu("PrefEtuRandom.txt")
                prefspe = f.lecture_preferences_spe("PrefSpeRandom.txt")
            

                #GS côté parcours
                start = time.time()
                f.GS_parcours_nouv(prefetu, prefspe, f.capacite("PrefSpeRandom.txt"))
                end = time.time()

                print("GS Masters Time " + str(end-start))
                sum_master += end-start

            avg_master = sum_master/10

            print("------------------------------")

            liste_n.append(n)
            liste_temps.append(avg_master)
            n+= 200

def courbe_GS(gs):
        
        x = []
        y = []

        gs(x,y)

        plt.xlabel("n")
        plt.ylabel("tmp")
        plt.plot(x,y)

        plt.xlabel("Nombre n d'étudiants")
        plt.ylabel("Temps de calcul moyen")

        plt.savefig("résultats.png")
        plt.show()


"""   
def nb_iterationsGS(n,x,y,gs):
    cpt = 0
    for i in range(10):

        mat.pref_etu_random(n)
        mat.pref_spe_random(n)

        prefetu = f.lecture_preferences_etu("PrefEtuRandom.txt")
        prefspe = f.lecture_preferences_spe("PrefSpeRandom.txt")

        if gs == "etu":
            f.GS_etudiants_nouv(prefetu, prefspe, f.capacite("PrefSpeRandom.txt"))
        else:
            f.GS_parcours_nouv(prefetu, prefspe, f.capacite("PrefSpeRandom.txt"))
    x.append(n)
    y.append(cpt/10)


def courbe_calcul_iteration(gs):
    x = []
    y = []
"""

         


courbe_GS(temps_calcul_GS_etudiant)