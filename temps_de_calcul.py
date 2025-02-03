import time
import matrices_aleatoires as mat
import fonctions as f

n = 200

while n<=200:
    #Rajout des intructions

    #Tests 10 par n
    for i in range(10): 

        #Définition des données
        mat.pref_etu_random(n)
        mat.pref_spe_random(n)

        prefetu = f.lecture_preferences_etu("PrefEtuRandom.txt")
        prefspe = f.lecture_preferences_spe("PrefSpeRandom.txt")

        print(prefetu)

        #GS côté étudiants
        start = time.time()
        f.GS_etudiants(prefetu,prefspe,"PrefSpeRandom.txt")

        end = time.time()
        print("GS Etudiants " + str(end-start))

        #GS côté parcours
        start = time.time()
        print(prefspe)
        f.GS_parcours(prefetu, prefspe, "PrefSpeRandom.txt")
        end = time.time()

        #Calcul du temps
        print("GS Parcours ", str(end-start))


    n+= 200
    
