#Day-05 of 100 Days of Coding
#November 23, 2020
#Shazid Hasan Riam

#for loop with lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie\n\n")

#for loop with range
for number in range(1, 10):
    print(number)

for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)