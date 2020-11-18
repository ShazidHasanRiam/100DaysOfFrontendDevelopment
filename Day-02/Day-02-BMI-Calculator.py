#Day-02 of 100 Days of Coding
#November 19, 2020
#Shazid Hasan Riam

height = input("Enter Your Height in M: ")
weight = input("Enter Your Weight in KG: ")

bmi = int(weight) / float(height) ** 2

bmi_as_int = int(bmi)

print(bmi)
print(bmi_as_int)