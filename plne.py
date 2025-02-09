import fonctions as fun
#script qui permet de generer un fichier .lp
def write(str_content, output_file):

    file = open(output_file, "w")
    file.write(str_content)
    file.close()

k = 3

res = "Maximise\n"
prefetu = fun.lecture_preferences_etu("PrefEtu.txt")
prefspe = fun.lecture_preferences_spe("PrefSpe.txt")
capacite = fun.capacite("PrefSpe.txt")

tabdistpref =[[0 for _ in range(len(prefetu[0]))] for _ in range (len(prefetu))]

for x in range(len(prefetu)) :
    for dist in range(len(prefetu[0])):
        a = prefetu[x][dist]
        tabdistpref[x][a] +=dist

res+= "obj :"
contraintes1 ="Subject To\n" #vérifie que chaque étudiant n'est affécté qu'a un seul master
contraintes2 = "" #vérifie que les masters ne dépassent pas leur capacité
contraintes3 = "" #vérifie que l'on ne prends bien que dans les k masters préférés
bounds = "" 
binary = ""
for i in range(len(prefetu)):
    contraintes1+="c"+str(i+1)+": "
    for j in range(len(prefetu[0])):
        res+= str(tabdistpref[i][j])+" x"+str(i)+str(j)+" + "
        contraintes1+= " x"+str(i)+"_"+str(j)+" + "
        contraintes3+= str(tabdistpref[i][j])+" x"+str(i)+"_"+str(j)+ " + "
        bounds+= "0 <= x"+str(i)+"_"+str(j)+" <= 1\n"
        binary += "x"+str(i)+"_"+str(j) +" "
        if j== len(prefetu[0])-1:
            contraintes1 = contraintes1[:-3]+" = 1\n"
            contraintes3 = contraintes3[:-3]+" <= "+str(k)+"\n"
            
    
res = res[:-3]
for j in range(len(prefetu[0])):
    contraintes2+="c"+str((len(prefetu))+j+1)+": "
    for i in range(len(prefetu)):
        contraintes2+= str(tabdistpref[i][j])+" x"+str(i)+"_"+str(j)+" + "
        if i== len(prefetu)-1:
            contraintes2 = contraintes2[:-3]+" <= "+ str(capacite[j])+"\n"

res += contraintes1 + contraintes2 + contraintes3
res+="Bounds\n"+bounds
res+="Binary\n"+binary
res+="\nEnd"

write(res, "PLNE1.ld")





print(res)
#print(contraintes1)
#print(contraintes2)
#print(contraintes3)

"""for a in range(len(prefspe)) :
    for dist in range(len(prefspe[0])):
        x = prefspe[a][dist]
        tabdistpref[x][a] +=dist"""



