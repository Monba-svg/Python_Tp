
# Exercice 1 : Opérations de base 
# Écrire un programme qui déclare deux variables a = 15 et b = 4, puis affiche : 
# - La somme de a et b 
# La différence a - b - 
# Le produit a * b - Le quotient exact a / b 
# - Le quotient entier a // b -
# Le reste de la division euclidienne a % b 
# a à la puissance b 
print("Exercice 1")
a = 15
b = 4
print(f"La somme entre {a} et {b} est de : {a+b}")
print(f"La difference entre {a} et {b} est de : {a-b}")
print(f"Le produit entre {a} et {b} est de : {a*b}")
print(f"Le quotient exact de {a} par {b} est de : {a/b}")
print(f"Le quotient entier de {a} par {b} est de : {a//b}")
print(f"Le modulo de {a} par {b} est de : {a%b}")
print(f" {a} à la puissance {b} est de : {a**b}")

# Exercice 2 : Affectation multiple 
# Écrire un programme qui : - Déclare une variable x = 10 
# - Ajoute 5 à x (en utilisant +=) 
# - Multiplie x par 2 (en utilisant *=) 
# - Affiche la valeur finale de x
print("Exercice 2")
x=10
x+=5
print("Ajoutons 5 à x on a donc : x =",x) 
x*=2
print("Multiplions x par 2 on a donc comme valeur finale : x =",x) 

# Exercice 3 :
# Écrire un programme qui demande à l’utilisateur une température en degrés Celsius (via 
# input()), puis affiche la température équivalente en Fahrenheit avec la formule :   
# F = C * (9/5) + 32
# print("Saisir la température de votre choix")
# t = input()
# temp_r = float(t) * (9/5) + 32
# print(f"{t}°C équivaut à {temp_r}F")

# Exercice 4 : Calcul d’aire 
# Demander à l’utilisateur la longueur et la largeur d’un rectangle (en mètres). Calculer et 
# afficher son aire en m². 
# print("Saisir la longueur de votre rectangle en metre")
# L=int(input())
# print("Saisir la largeur de votre rectangle en metre")
# l=int(input())
# print(f"l'aire de votre rectangle est de {L*l} m2")


# Exercice 5 : Moyenne de trois notes 
# Demander à l’utilisateur trois notes (entre 0 et 20).
# Calculer leur moyenne et l’afficher avec 
# deux décimales. 
print("saisir trois notes compris entre 0 et 20")
nota=0
it=0
while  it<3 :
        
        note=float(input())
        if (note>0 and note<20):
                nota = nota + note
        else :
         print("la note doit etre comprise entre 0 et 20")
         break
        it+=1
    
    
        
       
print(f"la moyenne est de {nota/3:.2f}")
    



