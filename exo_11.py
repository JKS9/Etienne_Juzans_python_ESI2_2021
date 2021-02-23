print("Exo 11 :")
array = ["chat", "chien", "poule","vache", "cochon", "ane", "canard", "chevaux"]

print(array)

value = input("value search : ")

i = 0
nb_loop = len(array)

while i <= nb_loop:

  if value == array[i]:

    strings = str(i)
    print("l'index à rechercher est :"+ strings)
    break
  
  i += 1
