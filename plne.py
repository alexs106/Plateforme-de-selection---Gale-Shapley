import fonctions as fun
#script qui permet de generer un fichier .lp
def write(str_content, output_file):

    file = open(output_file, "w")
    file.write(str_content)
    file.close()

k = 5

res = "Maximise\n"
prefetu = fun.lecture_preferences_etu("PrefEtu.txt")
prefspe = fun.lecture_preferences_spe("PrefSpe.txt")
capacite = fun.capacite("PrefSpe.txt")

tabdistpref =[[0 for _ in range(len(prefetu[0]))] for _ in range (len(prefetu))]

for x in range(len(prefetu)) :
    for dist in range(len(prefetu[0])):
        a = prefetu[x][dist]
        tabdistpref[x][a] +=dist

pe = tabdistpref

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
        contraintes2+= " x"+str(i)+"_"+str(j)+" + "
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

#Question 14

pm = [[0 for _ in range(len(prefetu[0]))] for _ in range (len(prefetu))]

for a in range(len(prefspe)) :
    for dist in range(len(prefspe[0])):
        x = prefspe[a][dist]
        tabdistpref[x][a] +=dist
        pm[x][a] += dist

res2 = "Maximise\n"

res2+= "obj :"
contraintes11 ="Subject To\n" #vérifie que chaque étudiant n'est affécté qu'a un seul master
contraintes22 = "" #vérifie que les masters ne dépassent pas leur capacité
#contraintes3 = "" #vérifie que l'on ne prends bien que dans les k masters préférés
bounds = "" 
binary = ""
for i in range(len(prefetu)):
    contraintes11+="c"+str(i+1)+": "
    for j in range(len(prefetu[0])):
        res2+= str(tabdistpref[i][j])+" x"+str(i)+str(j)+" + "
        contraintes11+= " x"+str(i)+"_"+str(j)+" + "
        #contraintes3+= str(tabdistpref[i][j])+" x"+str(i)+"_"+str(j)+ " + "
        bounds+= "0 <= x"+str(i)+"_"+str(j)+" <= 1\n"
        binary += "x"+str(i)+"_"+str(j) +" "
        if j== len(prefetu[0])-1:
            contraintes11 = contraintes11[:-3]+" = 1\n"
            #contraintes3 = contraintes3[:-3]+" <= "+str(k)+"\n"
            
    
res2 = res2[:-3]
for j in range(len(prefetu[0])):
    contraintes22+="c"+str((len(prefetu))+j+1)+": "
    for i in range(len(prefetu)):
        contraintes22+= " x"+str(i)+"_"+str(j)+" + "
        if i== len(prefetu)-1:
            contraintes22 = contraintes22[:-3]+" <= "+ str(capacite[j])+"\n"

res2 += contraintes11 + contraintes22 #+ contraintes3
res2+="Bounds\n"+bounds
res2+="Binary\n"+binary
res2+="\nEnd"

write(res2, "PLNE14.ld")

#question 15

res3 = "Maximise\n"

res2+= "obj :"
contraintes111 ="Subject To\n" #vérifie que chaque étudiant n'est affécté qu'a un seul master
contraintes222 = "" #vérifie que les masters ne dépassent pas leur capacité
contraintes333 = "" #vérifie que l'on ne prends bien que dans les k masters préférés
bounds = "" 
binary = ""
for i in range(len(prefetu)):
    contraintes111+="c"+str(i+1)+": "
    for j in range(len(prefetu[0])):
        res3+= str(tabdistpref[i][j])+" x"+str(i)+str(j)+" + "
        contraintes111+= " x"+str(i)+"_"+str(j)+" + "
        contraintes333+= str(pe[i][j])+" x"+str(i)+"_"+str(j)+ " + "
        bounds+= "0 <= x"+str(i)+"_"+str(j)+" <= 1\n"
        binary += "x"+str(i)+"_"+str(j) +" "
        if j== len(prefetu[0])-1:
            contraintes111 = contraintes111[:-3]+" = 1\n"
            contraintes333 = contraintes333[:-3]+" <= "+str(k)+"\n"
            
    
res3 = res3[:-3]
for j in range(len(prefetu[0])):
    contraintes222+="c"+str((len(prefetu))+j+1)+": "
    for i in range(len(prefetu)):
        contraintes222+=" x"+str(i)+"_"+str(j)+" + "
        if i== len(prefetu)-1:
            contraintes222 = contraintes222[:-3]+" <= "+ str(capacite[j])+"\n"

res3 += contraintes111 + contraintes222 + contraintes333
res3+="Bounds\n"+bounds
res3+="Binary\n"+binary
res3+="\nEnd"

write(res3, "PLNE15.ld")

print(res3)

