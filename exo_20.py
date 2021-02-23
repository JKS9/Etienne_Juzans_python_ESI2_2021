print("Exo 19 :")
import requests

r = requests.get('https://restcountries.eu/rest/v2/region/europe')

nb = len(r.json())
print(nb)
i = 0
while i <= nb -1:
  nb_population = str(r.json()[i]["population"])
  print(r.json()[i]["name"])
  print("nombre de population : "+ nb_population)
  print("**********")
  i += 1
