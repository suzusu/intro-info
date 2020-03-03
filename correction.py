"""
Sujet :

Exercice 1 :
Afficher les nombres pairs de 4 à 16 avec une boucle.

Exercice 2 :
Définir une liste contenant les noms des jours de la semaine. Afficher le troisième élement de la liste (c’est-à-dire Mercredi).

Exercice 3 :
Définir un dictionnaire qui associe à chaque mois le nombre de jours. Afficher le nombre de jours pour Décembre.

Exercice 4 :
Télécharger la page www.wikipedia.fr. Afficher le message “erreur du serveur” si le code d’erreur est supérieur ou égal à 500.
"""

# Exercice 1

for compteur in range(4, 17, 2):
    print(compteur)

# Exercice 2

liste_jours = ['Lundi', 'Mardi', 'Mercredi',
    'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

print(liste_jours[2])

# Exercice 3

nb_jours_mois = {
    'Janvier': 31,
    'Février': 28,
    'Mars': 31,
    'Avril': 30,
    'Mai': 31,
    'Juin': 30,
    'Juillet': 31,
    'Août': 31,
    'Septembre': 30,
    'Octobre': 31,
    'Novembre': 30,
    'Décembre': 31,
}

print(nb_jours_mois['Décembre'])

# Exercice 4

import requests

reponse = requests.get('https://www.wikipedia.fr')

if response.status_code >= 500:
    print('erreur du serveur')
