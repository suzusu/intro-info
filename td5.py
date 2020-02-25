# Pour une liste de nombres, comment calculer la somme des nombres ? Et le produit des nombres ? Déterminer le maximum et le minimum ?

Accumulateur = 0
Nombres = [1, 2, 3, 4, 5]

for nbr in Nombres:
    Accumulateur += nbr

print(Accumulateur)

# Autre solution

Nombres = [1, 2, 3, 4, 5]
print(sum(Nombres))

# Minimum

Nombres = [4, 7, 2]
minimum = Nombres[0]
for i in Nombres:
    if i < minimum:
        minimum = i
print(minimum)

# Les éléments d’une liste peuvent être de tout type. Ils peuvent même être des listes. Créer et afficher une liste de 10 éléments, chaque élément étant une liste de 4 éléments.

liste = [
    [1, 2, 3, 4], 
    [1, 2, 3, 4], 
    [1, 2, 3, 4], 
    [1, 2, 3, 4], 
    [1, 2, 3, 4], 
    [1, 2, 3, 4], 
    [1, 2, 3, 4], 
    [1, 2, 3, 4], 
    [1, 2, 3, 4], 
    [1, 2, 3, 4], 
]
