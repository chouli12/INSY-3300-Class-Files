#3-6
age=int(input("Enter Age: "))

if age<30:
    print("age is less than 30")
    print(age, "\n")
    
print('-----end-----')

#-------------------------------------------------------------
#3-10 (Single alternative decision structure)

# This program gets three test scores and displays
# their average.  It congratulates the user if the
# average is a high score.

# The HIGH_SCORE is a named-constant that holds the value
# considered a high score.
HIGH_SCORE = 95
 
# Get the three test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is', f'{average:.2f}')

# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')
    
#-----------------------------------------------------------------

#3-13 (Dual alternative decision structure)

# Named-Constants for base hours and overtime multiplier

BASE_HOURS = 40       # Base hours per week
OT_MULTIPLIER = 1.5   # Overtime multiplier

# Get the hours worked and the hourly pay rate.
hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

# Calculate and display the gross pay.
if hours > BASE_HOURS:
    # Calculate the gross pay with overtime.
    # First, get the number of overtime hours worked.
    overtime_hours = hours - BASE_HOURS

    # Calculate the amount of overtime pay.
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

    # Calculate the gross pay.
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
    
else:
    # Calculate the gross pay without overtime.
    gross_pay = hours * pay_rate

# Display the gross pay.
print(f'The gross pay is ${gross_pay:,.2f}.')

#----------------------------------------------------------------------

# 3-16 (Comparing Strings)

# This program compare strings with the < operator.
# Get two names from the user.
name1 = input('Enter a name (last name first): ')
name2 = input('Enter another name (last name first): ')
    
# Display the names in alphabetical order.
print('\nHere are the names, listed alphabetically:')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)

#----------------------------------------------------------------------

# 3-17 & 18 (Nested if )
# This program determines whether a bank customer
# qualifies for a loan.

MIN_SALARY = 30000.0  # The minimum annual salary
MIN_YEARS = 3        # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
                         'years employed: '))

# Determine whether the customer qualifies.
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You must have been employed', \
              'for at least', MIN_YEARS, \
              'years to qualify.')
else:
    print(f'You must earn at least $'
          f'{MIN_SALARY:,.2f} '
          f'per year to qualify.')


#----------------------------------------------------------------------

# 3-20 (elif)
# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Named-Constants to represent the grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade using Nested IF
if score >= A_SCORE:
    print('Your grade is A.')
else:
    if score >= B_SCORE:
        print('Your grade is B.')
    else:
        if score >= C_SCORE:
            print('Your grade is C.')
        else:
            if score >= D_SCORE:
                print('Your grade is D.')
            else:
                print('Your grade is F.')


# Determine the grade using elif
if score >= A_SCORE:
   grade = 'A'
elif score >= B_SCORE:
   grade = 'B'
elif score >= C_SCORE:
   grade = 'C'
elif score >= D_SCORE:
   grade = 'D'
else:
   grade = 'F'

 
print("Student Grade is:", grade)

#-----------------------------------------------------------------------------

#3-29
sales=float(input("Enter your sales amount: "))

if sales >= 10000.00:       # set the sales_quota_met flag
    sales_quota_met = True  # Boolean variable set to True
else:
    sales_quota_met = False # Boolean variable set to False

if sales_quota_met:     # this is equivalent to "if sales_quota_met == True:"
    print("Congratulations! You have met your sales quota!")
else:
    print("Sorry you have not met your sales quota")


#------------------------------------------------------------------------

#3-30 to 3-38
# Hit the Target Game
import turtle

# Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target
FORCE_FACTOR = 30     # Arbitrary force factor
PROJECTILE_SPEED = 1  # Projectile's animation speed
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
EAST = 0              # Angle of east direction
WEST = 180            # Angle of west direction

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
angle = turtle.numinput("Input","Enter the projectile's angle",
                        minval=0, maxval=360)
force = turtle.numinput("Input", "Enter the launch force (1-10)",
                        minval=1, maxval=10)

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target hit!')
else:
        print('You missed the target.')

