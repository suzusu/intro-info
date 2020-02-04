import requests 
import json 

resultat = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Paris&units=metric&APPID=281f2f47a07f35357ba3cefcc47c7f52")

texte = resultat.text

objets = json.loads(texte)

print(objets['main']['temp'])

#print(objets)

weather = objets['weather']

#print(weather)

premier_element = weather[0]

#print(premier_element)
#print(type(premier_element))

print(premier_element['description'])
