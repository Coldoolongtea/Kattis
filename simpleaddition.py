# PROBLEME : SIMPLE ADDITION - DIFFICULTE : 2.0


# DESCRIPTION
#Dans ce problème il faut effectuer la somme de deux entiers positifs

# SUBTILITES
#Les entiers peuvent être très grands et sont limités par le temps et la mémoire

# METHODE
#Les entrées saisies seront transformées en liste d'entiers, en veillant à 
#Se débaraser du retour à la ligne, la somme est ensuite effectuée dans le print
#Afin de ne pas utiliser de la mémoire pour sauvegarder le résultat




import sys


text=list(map(int,sys.stdin.read().replace("\n"," ").split()))
print(text[0]+text[1])  