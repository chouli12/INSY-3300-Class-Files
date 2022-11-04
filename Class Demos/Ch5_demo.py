#5-9
# function header defines a function name
def message():
    print("Hello World")
    print("Bye!\n")

# call the message() function
message()       # call the function message()
print ("Good Bye!")

#-------------------------------------------------------------------------

#5-12  Use of main function - best practice

def main():                 # define the main function
    print("Message for you....\n\n")
    
    message()               # call the message function

    print("Good Bye!")

def message():               # define a function named message
    print("Hello World")
    print("Bye!\n\n")

# call the main function
main()                      # first executable statement

# If you use a main function,
#      this is typically the only executable statement
                            

#-------------------------------------------------------------------------

#5-17  Use of pass keyword

def step1():    # empty function
    pass
def step2():    # empty function
    pass

step1()

# ---------

name="Joe"
if name=="Joe":
    pass       # used as a placeholder
else:
    print ("Name is not Joe")

#-------------------------------------------------------------------------

#5-18   Local Variables
# This program demonstrates two functions that
# have local variables with the same name.

def main():
    # Call the texas function.
    texas()

    # will be an error to access birds
    print("Texas has", birds, "birds.") 
    
    # Call the california function.
    california()

# Definition of the texas function. It creates
# a local variable named birds.
def texas():
    birds = 5000
    print("Texas has", birds, "birds.")

# Definition of the california function. It also
# creates a local variable named birds.
def california():
    birds = 8000    #try commenting out to see if you can access
                    # birds variable from texas() function
    print("California has", birds, "birds.")

# Call the main function.
main()

#-------------------------------------------------------------------------

#5-21
# This program demonstrates an argument being
# passed to a function.

def main():
    value = 5
    show_double(value)
    
# The show_double function accepts an argument
# and displays double its value.
def show_double(number):
    result = number * 2
    print(result)

# Call the main function.
main()

#-------------------------------------------------------------------------

#5-24
# This program demonstrates a function that accepts
# two arguments.

def main():
    print('The sum of 12 and 45 is')
    show_sum(12,20)

# The show_sum function accepts two arguments
# and displays their sum.
def show_sum(num1, num2):
    result = num1 + num2
    print(result)

# Call the main function.
main()

#-------------------------------------------------------------------------

#5-26
# This program demonstrates what happens when you
# change the value of a parameter.

def main():
    value = 99
    print(f'The value is {value}.\n')
    change_me(value)
    print(f'Back in main the value is {value}.')

def change_me(value):
    print('I am changing the value.')
    value = 0
    print(f'Now the value is {value}.\n')

# Call the main  function.
main()

#-------------------------------------------------------------------------

#5-29
# This program demonstrates keyword arguments.

def main():
    # Show the amount of simple interest using 0.01 as
    # interest rate per period, 10 as the number of periods,
    # and $10,000 as the principal.
    show_interest(10000, 0.01, 10)    # default sequence of arguments
    #show_interest(rate=0.01, periods=10, principal=10000.0)


    # show_interest(1000, periods=10, rate=0.01)
    # show_interest(10000, rate=0.01, 10)  # error - positional arguments first
    # show_interest(10000, 0.01, periods=10)
    # show_interest(10000, 0.01)

# The show_interest function displays the amount of
# simple interest for a given principal, interest rate
# per period, and number of periods.

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print(f'The simple interest will be ${interest:,.2f}.')

#def show_interest(principal, rate, periods=5):
#    interest = principal * rate * periods
#    print(f'The simple interest will be ${interest:,.2f}.') 

# Call the main function.
main()

#-------------------------------------------------------------------------

#5-30
# Create a global variable.
number = 0

def main():
    #global number    # declaring global variable to change its value
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print(f'The number you entered is {number}.')

# Call the main function.
main()

#-------------------------------------------------------------------------

#5-32
# Create a global constant.
INTEREST_RATE = 0.05

def main():
    global INTEREST_RATE
    INTEREST_RATE=0.2
    principal = float(input('Enter the Principal amount: '))
    computeInterest(principal)

def computeInterest(principal):
    print(f'The interest is {principal*INTEREST_RATE:.2f}.')

# Call the main function.
main()

#-------------------------------------------------------------------------
#5-40 and 41 Random functions

import random
for i in range(20):
    print(random.randint(1,10))

for i in range(20):
    print(random.randrange(2,10,3))

for i in range(20):
    print(random.random())

for i in range(20):
    print(random.uniform(2.0,10.5,0.5))


#-------------------------------------------------------------------------
#5-42 Random Seed example

import random
# Run with the same seed to generate same sequence
random.seed(10) 
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))

#-------------------------------------------------------------------------
#5-44
# This program calculates a retail item's sale price

# DISCOUNT_PERCENTAGE is used as a global constant
DISCOUNT_PERCENTAGE = 0.20

def main():
    reg_price = get_regular_price() # Get the item's regular price.
    sale_price = reg_price - discount(reg_price)  # Calculate the sale price.
    print(f'The sale price is ${sale_price:,.2f}.') # Display the sale price.

def get_regular_price():
    price = float(input("Enter the item's regular price: "))
    return price

def discount(price):
    return price * DISCOUNT_PERCENTAGE

# Call the main function.
main()

#-------------------------------------------------------------------------

#5-49
def main():
    number = int(input("Enter a number: "))
    if is_even(number):
        print("Even Number")
    else:
        print("Odd Number")

def is_even(number):
    if (number % 2) == 0:  # should be an even number if remainder is zero
        return True
    else:
        return False

main()

#-------------------------------------------------------------------------

#5-50  return more than one value  
def getName():
    FName=input("First Name: ")
    LName=input("Last Name: ")
    return ( FName, LName )

def main():
    firstName, lastName = getName()
    print(firstName, lastName)

main()

# ----------------------------------------------------
#Practice Code Examples:
# P1
def pass_it (a, b):
    x = b ** a
    return (x)

def main():
    num1 = 2
    num2 = 3
    answer = pass_it (num1, num2)
    print (answer)

main()
#------------------------------------------------------
#P2
def add(a,b):
    return a * b
    return a + b

print ( add(2,3) )

#------------------------------------------------------
#P3
def myfunc(num):
    while num > 0:
        num = num - 1

def main():
    num=1
    print(myfunc(num))

main()

#------------------------------------------------------
#P4
def add(num):
    return num + 3

def sub(num):
    return num - 2

print ( add(2) * sub(3) )

#------------------------------------------------------
#P5
def pass_it(x, y):
    return(x+y*3)

def main():
    str1 = "abc"
    str2 = "def"
    str3 = pass_it(str1, str2)
    print (str3)

main()

#------------------------------------------------------
#P6
def pass_it(x, y):
    z = y**x
    result = double(z)
    return(result)

def double(number):
    z= number * 2
    return(z)

def main():
    num1 = 2
    num2 = 4
    result=pass_it(num1, num2)
    print(result)

main()

#-------------------------------------------------------



