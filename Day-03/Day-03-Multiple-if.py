#Day-03 of 100 Days of Coding
#November 20, 2020
#Shazid Hasan Riam

print("Welcome to the Rollercoaster")
height = int(input("What is your height in CM? "))

if height >= 120:
    print("Congratulations! You can ride the Rollercoaster.")
    age = int(input("What is your age? "))
    if age <12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = (input("Do You want a photo taken? Y or N\n"))
    if wants_photo == "Y":
        bill += 3
    print(f"Your Final Bill Is: {bill}")

else:
    print("Sorry, You have to grow taller before you can ride.")
