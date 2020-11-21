#Day-04 of 100 Days of Coding
#November 21, 2020
#Shazid Hasan Riam

import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
