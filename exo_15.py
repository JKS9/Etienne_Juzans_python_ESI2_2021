print("Exo 15 :")

def function (chaine1, chaine2):

  len_chaine1 = len(chaine1)
  len_chaine2 = len(chaine2)

  if len_chaine1 == len_chaine2:
    print(chaine1)
    print(chaine2)

  elif len_chaine1 > len_chaine2:
    print(chaine1)

  else:
    print(chaine2)


text1 = input("text 1 : ")
text2 = input("text 2 : ")
function(text1, text2)  