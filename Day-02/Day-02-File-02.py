#Day-02 of 100 Days of Coding
#November 19, 2020
#Shazid Hasan Riam

#Practice
print(8/3)
print(round(8/3))
print(round(8/3, 2))
print(8//3)
# print(type(8//3))
result = 4 / 2
result /= 2
print(result)
#F String
score = 0
height = 1.5
isWinning = True

print(f"Your Score Is: {score}, \n"
      f"Your Height Is: {height},\n"
      f"Your Are Winning Is: {isWinning}")

#Exercise
age = input("What is your current age? ")
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months, and {years_remaining} years left")

