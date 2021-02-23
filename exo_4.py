print("Exo 4 :")
print("n1 and n2 must be between 0 and 20")

x = int(input("x: "))
y = int(input("y: "))

loop = 5

array_x = []
array_y = []

i = 0
while i<=loop:
    if i == 5:
        value = i * y

        print(value)
        array_x.append(value)
        array_y.append(value)
    else :
        value_neutre = i
        array_x.append(value_neutre)
        array_y.append(value_neutre)

    i += 1

print(array_x)
print(array_y)