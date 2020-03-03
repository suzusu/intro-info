# Créer la variable table_multiplication qui est une liste de listes telle que table_multiplication[i][j] est un nombre égal au produit de i et de j.

# Solution 1

table = []
for i in range(11):
    table.append([x for x in range(11)])
    for j in range(11):
        table[i][j] = i * j

print(table[3][5])

# Solution avec seulement "append"

table = []
for i in range(11):
    ligne = []
    for j in range(11):
        ligne.append(i*j)
    table.append(ligne)

print(table[3][5])

# Par compréhension (avancé)

table = [
    [i*j for j in range(11)]
    for i in range(11)
]

print(table[3][5])
