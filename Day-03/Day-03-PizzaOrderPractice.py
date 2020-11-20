#Day-03 of 100 Days of Coding
#November 20, 2020
#Shazid Hasan Riam

print("Welcome to Pizza Deliveries!")

size = input("What Size Pizza Do You Want? S, M or L ")
add_pepperoni = input("Do You Want Pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your Final Bill Is ${bill}")
