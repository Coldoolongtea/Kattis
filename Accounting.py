# PROBLEME : ACCOUNTING - DIFFICULTE : 5.0


# DESCRIPTION
# Le problème consiste à garder un nombre pour chaque personne 
# qui correspond à sa fortune.
# Trois types d’instructions peuvent êtres rencontrés 
# Set i x : ce qui signifie que la fortune de la personne i devient x
# Restart x :la fortune de tous les utilisateurs vaut x
# Print i : la fortune de l’utilisateur i est affichée



# SUBTILITES
# Étant donnée qu'il y a beaucoup d'instruction et d'utilisateurs 
# la contrainte de temps joue un rôle important

# METHODE

# Sauvegarder la position des utilisateurs à qui nous avons modifié 
# la fortune depuis le dernier dans un set reset nous permettra de les 
# retrouver plus rapidement si la personne n'est pas dans le set sa fortune 
# est équivalente au nombre correspondant au dernier reset




import sys


#La valeur au derneir reset
number=0
#les indices des personnes qui ont vu leurs fortunes changer entre resets
changed = set()
#les entrées sont transformées en liste d'entiers
N,Q = list(map(int,sys.stdin.readline().split()))
#Au départ tous les utilisateurs ont une fortune de 0
numbers = [0]*N
for i in range(Q):
        line = sys.stdin.readline().split()     
        #Si l'instruction est set
        if line[0][0]=='S':
            #On modifie la valeur de fortune de la personne en question
            numbers[int(line[1])-1]=int(line[2])
            #On sauvegarde sa position dans un set
            changed.add(int(line[1])-1)
        #Si nous devons imprimer la fortune d'une personne
        elif line[0][0]=='P':
            #On vérifie si son indice est dans le set
            if int(line[1])-1 in changed:
                #si oui on imprime sa fortune à partir de la liste
                print(numbers[int(line[1])-1])
            else:
               #si pas on imprime la dernière valeur du nombre resultant du reset
                print(number)
        else :
            #S'il faut faire un reset on sauvegarde le nombre et on vide le set
             number = int(line[1])
             changed.clear()
             

