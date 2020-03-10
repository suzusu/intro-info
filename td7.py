# Calcul de l'IMC

poids = int(input("Quel est votre poids en kg ?"))
taille = int(input("Quelle est votre taille en cm ?"))

imc = poids / (taille / 100) * 2

if imc <= 18:
    print('Attention : IMC bas')
if imc >= 25:
    print('Attention : IMC élevé')
