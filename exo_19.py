print("Exo 19 :")
import requests

r = requests.get('https://restcountries.eu/rest/v2/region/europe')

nb = len(r.json())
print(nb)
i = 0
while i <= nb -1:
  print(r.json()[i]["name"])
  print(r.json()[i]["subregion"])
  print("**********")
  i += 1
