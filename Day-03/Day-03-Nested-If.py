#Day-03 of 100 Days of Coding
#November 20, 2020
#Shazid Hasan Riam

print("Welcome to the Rollercoaster")
height = int(input("What is your height in CM? "))

if height >= 120:
    print("Congratulations! You can ride the Rollercoaster.")
    age = int(input("What is your age? "))
    if age <12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, You have to grow taller before you can ride.")
