"""
Sujet :

Exercice 1 :
Afficher les nombres impairs de 7 à 13 avec une boucle.

Exercice 2 :
Définir une liste contenant les chiffres romains de 1 à 10. Afficher l’élément III.

Exercice 3 :
Définir un dictionnaire qui associe à chaque jour de la semaine, s’il fait partie du week-end ou non. En utilisant ce dictionnaire, déterminer si jeudi fait partie du week-end.

Exercice 4 :
Télécharger la page www.wikipedia.fr. Afficher le message “erreur du serveur” si le code d’erreur est supérieur ou égal à 500.

"""

# Exercice 1

for compteur in range(7, 14):
    if compteur % 2 == 1:
        print(compteur)

for compteur in range(7, 14, 2):
    print(compteur)

# Exercice 2

liste_nombres = [
    'I', 'II', 'III', 'IV', 'V',
    'VI', 'VII', 'VIII', 'IX', 'X',
]

print(liste_nombres[2])

# Exercice 3

fait_partie_du_week_end = {
    'lundi': False,
    'mardi': False,
    'mercredi': False,
    'jeudi': False,
    'vendredi': False,
    'samedi': True,
    'dimanche': True,
}

if fait_partie_du_week_end['jeudi']:
    print('Jeudi est un jour du week-end')
else:
    print("Jeudi n'est pas un jour du week-end")

# Exercice 4

import requests

reponse = requests.get('https://www.wikipedia.fr')

if response.status_code >= 500:
    print('erreur du serveur')
