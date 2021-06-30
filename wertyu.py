# PROBLEME : WERTYU - DIFFICULTE : 3.0

# DESCRIPTION
#Dans ce problème il faut décoder un message en utilisant un
#décalage des letters sur un clavier QWERTY
#Si par exemple la lettre K est saisie nous devons savior qu'il s'agit d'un J
#Les espaces résante dans la saisie se trouvent inchangés dans l'affichage

# SUBTILITES
#Construire la phrase décodé en respectant les limites de temps et de mémoire

# METHODE
#Parcourir le string saisi caractère par caractère
#S'il y a un espace ou un retour à la ligne le caractère saisi est imprimé
#Si pas une recherche est effectuée dans une liste représentant un clavier QWERTY
#l'élément imprimé est alors celui qui se trouve avant le caractère saisi
#afin de pas construite le string et le sauvegarder en memoir un print est fait pour
#chaque caractère saisi, l'end="" premet d'éliminer les retours à la ligne


import sys





#Une liste qui représente le clavier QWERTY
Keyboard=["1234567890-=","QWERTYUIOP[]\"","ASDFGHJKL;'","ZXCVBNM,./"]


#Saisie des données
text=sys.stdin.read() 

#Parcourir les données 
for i in text:
        if i==" ":
            print(i,end="")
        elif i=="\n":
            print(i,end="")
        else:
          #si le caractère n'est pas un espace ou un retour à la ligne 
          #on imprime le caractère situé avant le caractère trouvé dans la liste Keyboard
            for l in range(len(Keyboard)):
                for p in range(len(Keyboard[l])):
                    if Keyboard[l][p]==i:
                        print(Keyboard[l][p-1],end="")