#Day-02 of 100 Days of Coding
#November 19, 2020
#Shazid Hasan Riam

print("Welcome To The Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# print(type(bill))
# print(type(tip))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each Person Should Pay ${final_amount}")