print("Exo 13 :")
import random
even = [ x for x in range(10) if x%2 == 0]

nb = len(even)

nb_random = random.randint(0, nb)

print(even[nb_random])