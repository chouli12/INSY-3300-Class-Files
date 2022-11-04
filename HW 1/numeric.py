# welcome statement and prompting user to input 
print("Welcome to Roman Numeral Converter", '\n')
num = int(input("Please Input a Number between 1 and 10: "))

# if elif statments to determine # and also error message for anything less or more than range
if num < 1 or num > 10:
    print("Error: Invalid Number")
elif num == 1:
    print('I')
elif num == 2:
    print('II')
elif num == 3: 
    print('III')
elif num == 4: 
    print('IV')
elif num == 5: 
    print('V')
elif num == 6: 
    print('VI')
elif num == 7:
    print('VII')
elif num == 8:
    print("VIII")
elif num == 9: 
    print('IX')
elif num == 10:
    print("X")