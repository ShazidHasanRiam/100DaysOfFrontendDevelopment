#Day-05 of 100 Days of Coding
#November 23, 2020
#Shazid Hasan Riam

for number in range(1, 101):
    if number % 3 ==0 and number % 5 == 0:
        print("FizzBuzz")
        #Divisible by both 3 and 5

    elif number % 3 == 0:
        print("Fizz")
        #Dividible by 3
    elif number % 5 == 0:
        print("Buzz")
        #Divisible by 5
    else:
        print(number)
