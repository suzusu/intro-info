

mois = ["Janvier", "Fevrier", "Mars", 'Avril', "Mai", 'Juin', 'Juillet', "Aout"]
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#attention, ce n'est pas équivalent à : nombres_str = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print(mois)
print(nombres)

# Quelques exemples d'utilisation de []

print(mois[3])
print(nombres[3])

print(mois[:3])
print(mois[3:])

print(mois[-3])
print(mois[-3:])

print(mois[2:4])

print(mois[2:-2])

# Le code suivant écrase la liste originale :

sauvegarde_mois = mois

print(mois.reverse())
print(mois)

print(sauvegarde_mois)

# Pour éviter la modification de la liste originale, il faut faire une copie :

import copy 

copie_mois = copy.copy(mois)

copie_mois.reverse()

print(copie_mois)
print(mois)

taille_liste = len(mois)
print(taille_liste)

# Dictionnaires

nb_jours = {
    "Janvier": 31,
    "Fevrier": 28,
    "Mars": 31,
}

print(nb_jours)

print(nb_jours["Mars"])

print(len(nb_jours))
