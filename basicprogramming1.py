# PROBLEME : BASIC PROGRAMMING - DIFFICULTE : 4.1

# DESCRIPTION

#Ce problème est composé de 7 sous problèmes l'action à effectuer 
#est déterminé par la valeur du nombre t saisi


#Problème t=1
#Imprimer 7

#Problème t=2
#comparer la première valeur de la liste saisie et imprimer "Bigger" 
#Si le première élément est plus grand que le deuxième et "smaller" s'il est plus petit
#Equal s'il est identique


#Problème t=3
#imprimer la médiane des 3 premières valeurs du saisi

#Problème t=4
#imprimer la somme des valeurs de la saisie

#Problème t=5
#imprimer la somme des valeurs pairs de la saisi

#Problème t=6
#Il faut déchiffrer un message qui est constitué des chiffres saisi
#Ceci est fait en attribuant à chaque lettre de l'alphabet un nombre
#Le modulo 26 du nombre saisi est alors recherché dans le dictionnaire afin de trouver
#La lettre correspondante

#Problème t=7
#Suivre le trajet les nombre dans le saisi
#imprimer "Cyclic" si on boucle


# SUBTILITES
#Contraintes de temps et de mémoire

# METHODE
#Utiliser des fonctions afin d'avoir un code facile à comprendre
#Utilisé des fonctions de base comme "sum" afin d'éviter les boucles 
#quand c'est possible




import statistics as st
import string
import sys


#La fonction pour t=1
def seven(numbers):
    print("7")
    
    
#La fonction pour t=2      
def compare(numbers):
    if numbers[0]>numbers[1]:
        print("Bigger")
    elif numbers[0]==numbers[1]:
        print("Equal")
    else:
        print("Smaller")
        
        
#La fonction pour t=3        
def med(A):
    #On prend la médiane des 3 entrées
    print(st.median([A[0],A[1],A[2]]))
  
    
#La fonction pour t=4  
def adding(A):
    print(sum(A))

#La fonction pour t=5    
def evenSum(A):
    #Creation d'une liste qui ne contient que les nombres pairs
    ev =[i for i in A if i%2==0]
    print(sum(ev))
    
    
    
#La fonction pour t=6    
def joining(A):
    #alpha est une liste de l'alphabet
    alpha=list(string.ascii_lowercase)
    numbers=list(range(0,27))    
    #creation d'un dictionnaire liant les lettres aux chiffres
    mapped=dict(zip(numbers,alpha))
    modeled=[i%26 for i in A]
    #On imprime le correspondant du modulo 26 de l'entrée dans le dictionnaire
    #en retirant le retour à la ligne 
    for i in modeled:
        print(mapped[i],end="")
        
        
        
#La fonction pour t=7    
def final(A):
    i=0
    i=A[i]
    
    N=len(A)
    #permet de voir si on est déjà passé à un endroit donné
    looping=[False for i in range(N)]
    
    while 1:
        
        if i > N-1 or i<0:
            print("Out")
            break
        elif  i == N-1:
            print("Done")
            break
        elif looping[i]==True:
            print("Cyclic")
            break
        #On met à jour la valeur looping ainsi nous serons la prochaine fois
        #Si nous avons déjà visité cette position là 
        looping[i]=True
        i=A[i]
        
    
    
#Options est un dictionnaire qui jouera un rôle
#équivalent d'un switch case 
options = {1 : seven,
           2: compare,
           3: med,
           4: adding,
           5: evenSum,
           6: joining,
           7:final
           
}


#Lecture et nettoyage des entrées
numbers = list(map(int,sys.stdin.read().split()))
commands=[numbers[0],numbers[1]]   
numbers=numbers[2:]
#On appelle la fonction correspondant à la deuxième commande donc t
options[commands[1]](numbers)

