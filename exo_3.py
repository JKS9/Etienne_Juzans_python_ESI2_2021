print("Exo 3 :")
n = int(input("n: "))
i = 0
disctionnaire = {}
while i<=n:
    value = (i * i)
    disctionnaire.update({i: value})
    i += 1

print(disctionnaire)