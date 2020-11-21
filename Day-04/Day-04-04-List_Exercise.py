#Day-04 of 100 Days of Coding
#November 21, 2020
#Shazid Hasan Riam

import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameAsCSV = input("Type all the names, Separated by comma. \n")
names = nameAsCSV.split(",")

#Get the total number of items in list
num_items = len(names)

#Generate random numbers between 0 and last index
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = random.choice(names)
#person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")

