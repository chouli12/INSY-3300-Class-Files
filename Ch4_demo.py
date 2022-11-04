# 4-5 and 4-6
count=1    # test with condition being 5 - pretest loop
while count<5:
    print('Iteration:', count)
    count=count+1
    
#------------------------------------------------------------------------ 
# 4-7
# This program calculates sales commissions.

# Create a variable to control the loop.
keep_going = 'y'

# Calculate a series of commissions.
while keep_going == 'y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the commission.
    commission = sales * comm_rate

    # Display the commission.
    print(f'The commission is ${commission:,.2f}.')

    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another ' +
                       'commission (Enter y for yes): ')    #try 'Y'
    

# 4-7 (another example of while loop)
# This program assists a technician in the process
# of checking a substance's temperature.

# Create a named-constant to represent the maximum
# temperature.
MAX_TEMP = 102.5

# Get the substance's temperature.
temperature = float(input("Enter the substance's Celsius temperature: "))

# As long as necessary, instruct the user to
# adjust the thermostat.
while temperature > MAX_TEMP:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')
    temperature = float(input('Enter the new Celsius temperature: '))

# Remind the user to check the temperature again
# in 15 minutes.
print('The temperature is acceptable.')
print('Check it again in 15 minutes.')

#-------------------------------------------------------------------------

#4-8 Infinite Loop
count=1    
while count<5:
    print('Iteration:', count)
    #count=count+1   # code to make the loop condition false at some point

#--------------------------------------------------------------------------

# 4-9
# This program demonstrates a simple 'for' loop
# that uses a list of numbers.

print('Display the numbers 1 through 5.')
for num in [1, 2, 3, 4, 5]:      # num is the 'target' variable
    print(num)
print('\n')

# 4-9 (another example with strings)
# This program also demonstrates a simple 'for'
# loop that uses a list of strings.

for fruit in ['orange', 'apple', 'pear']:
    print(fruit)

#-------------------------------------------------------------------------

# 4-11
for i in range(10):  # this range starts with 0 and ends at 9
    print(i)
    
for i in range(1,10):  # range does not include the ending limit
    print(i)

for i in range(2,10,2):  # range does not include the ending limit
    print(i)

#------------------------------------------------------------------------

# 4-12
for i in range(3,15,2):
    print(i, i**2)  # print the number and its square 

#------------------------------------------------------------------------
# 4-13
count=int(input("Enter the limit for the range: "))

for i in range(0,count):
    print(i)

#-----------------------------------------------------------------------
#4-14
for i in range(15,3,-2):    # negative step value
    print(i, i**2)  # print the number and its square 

# try with starting value lower than ending limit
for i in range(3,15,-2):    # negative step value
    print(i, i**2)  # print the number and its square 



# print fun strings of *'s
for i in range(10):
    print (i*"*")

# print fun strings of *'s
for i in range(1,11):
    print (f'{i * "*":10}', f'{i * "*":>10}')
for i in range(9,0,-1):
    print (f'{i * "*":10}', f'{i * "*":>10}')
        
#--------------------------------------------------------------------------
# 4-15 & 16
# This program calculates the sum of a series
# of numbers entered by the user.

# Initialize an accumulator variable.
total = 0.0

# Explain what we are doing.
print('This program calculates the sum of ', end='')
print('numbers you will enter until you enter 0 to stop')

number = float(input("Enter a number or enter 0 to end: "))
   
# Get the numbers and accumulate them till 0 is entered to stop
while number != 0:
    total = total + number
    number = float(input("Enter a number or enter 0 to end: "))

# Display the total of the numbers.
print(f'The total is {total}.')

#--------------------------------------------------------------------------
# 4-18
# Augmented assignment operators
total = 0
total = total + 10
print (total)

total += 10   # same as total=total+10
print (total)

total /= 10 # same as total=total/10
print (total)

#--------------------------------------------------------------------------
# 4-19 - Sentinel
# same example as 4-15 where 0 is used as sentinel value to stop the loop

#--------------------------------------------------------------------------
# 4-21 and 22
# Get a test score
score = int(input("Enter a valid test score between 0 and 100: "))
# Validate the test score to be not less than 0 or greater than 100
while score <0 or score >100:
    print ("ERROR: Score can't be negative or more than 100")
    score = int(input("Enter the correct score: "))

print ("Score is", score)

#--------------------------------------------------------------------------
# 4-23 Nested loop
for i in range(3):
    print('Outer Loop Iteration',i)
    for j in range(2):
        print('Inner Loop Iteration', j, 'i=',i,'j=',j)
    print('\n')


# print fun strings of *'s - Using Nested Loops
iterations=int(input("Enter the number of loops/iternations: "))
for x in range(iterations):    # nested loop
    print(20*" ", " Loop:", x+1)
    for i in range(1,11):
        print (f'{i * "*":10}', f'{i * "*":>10}')
    for i in range(9,0,-1):
        print (f'{i * "*":10}', f'{i * "*":>10}')
    

#--------------------------------------------------------------------------
# 4-28
# This program draws a design using repeated circles.
import turtle

# Named constants
NUM_CIRCLES = 36    # Number of circles to draw
RADIUS = 100        # Radius of each circle
ANGLE = 10          # Angle to turn
ANIMATION_SPEED = 0 # Animation speed

# Set the animation speed.
turtle.speed(ANIMATION_SPEED)

# Draw 36 circles, with the turtle tilted
# by 10 degrees after each circle is drawn.
for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

#--------------------------------------------------------------------------
# 4-29
# This program draws a design using repeated lines.
import turtle

# Named constants
START_X = -200      # Starting X coordinate
START_Y = 0         # Starting Y coordinate
NUM_LINES = 36      # Number of lines to draw
LINE_LENGTH = 400   # Length of each line
ANGLE = 170         # Angle to turn
ANIMATION_SPEED = 8 # Animation speed

# Move the turtle to its initial position.
turtle.hideturtle()
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()

# Set the animation speed.
turtle.speed(ANIMATION_SPEED)

# Draw 36 lines, with the turtle tilted
# by 170 degrees after each line is drawn.
for x in range(NUM_LINES):
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)





