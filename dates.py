# Greeting the user.. with nice greeting.
print("Welcome to the Magic Date Finder", '\n')

# promting the user to enter desired information to complete calculation
month = int(input("Please enter a month.. EX: 1-12:  "))
day = int(input("Please enter a day.. EX: 1-31:  "))
year = int(input("Please enter the year.. EX: 00-99:  "))

# print statement to identify the date.
print("The date you entered is:", month, '/', day, '/', year)

# calculations/ if elif statement to determine if the date is magical.
if (month * day) == year:
    print("This date is magical!!")
elif (month *day) != year:
    print("Sorry this date isnt Magical :(")