# Promopting user to input date: with example
leap_year = int(input("Please enter a year. EX: 2002: "))

# leap year calcuations nested if and elif statement 
if (leap_year % 100 == 0):
    if (leap_year % 400 ==0):
        print(leap_year, "Thats a leap year! Febuary has 29 days.")
    else:
        print("Sorry", leap_year, "is not a leap year, Febuary has 28 days.")
elif (leap_year % 4 == 0):
    print(leap_year, "Thats a leap year! Febuary has 29 days.")
else:
    print("Sorry", leap_year, "is not a leap year, Febuary has 28 days.")






