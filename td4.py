# Exercice 1 : Afficher les nombres paires entre 0 et 30.

X = 0
for compteur in range(16):
    print(X)
    X = X + 2

# Exercice 2 : Afficher en ordre décroissant les nombres de 10 à 1.

x = 10
while x != 0:
    print(x)
    x = x - 1

# Exercice 3 : Calculer 1 x 2 x 3 x 4 x 5 x 6 avec une boucle.

y = 1
for x in range(6):
    y = y * (x+1)
print(y)

# Exercice 4 : Pour chaque nombre entre 1 et 30, afficher si le nombre est pair ou impair.

while True:
    pass

# Exercice 5 : bloucles imbriquées

noms = ["Paul", "Rose", "Etienne"]
phrases = ["Bonjour", "Comment vas-tu", "Au revoir"]
for comb1 in phrases:
    for comb2 in noms:
        print(comb1 + " " + comb2)

# Exercice 6 : années bisextiles

annee = int(input("Quelle est l'année"))
x = annee % 4
y = annee % 100
z = annee % 400

if x != 0:
    print("non bisextile")
if z == 0:
    print("bisextile")
if y == 0 and z != 0:
    print("non bisextile")
if x == 0 and y != 0:
    print("bisextile")
