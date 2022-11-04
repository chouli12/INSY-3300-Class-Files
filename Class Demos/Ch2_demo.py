# Slide 2-11
print('John Doe')           
print("123, Uta Drive")     
print('Arlington,TX-76001')

# 2-12
print("How's it going?")
print('How"s it going?')

print("""How's it going "Mr. Doe" ? """)

#2-13
# print name and address
print('John Doe')           # Display name
print("123, Uta Drive")     # Display address
print('Arlington,TX-76001') # Display City, state and ZIP

#2-15
age = 29
print (age)

age=29
print ('age')

print(name)    #unassigned variable - value not assigned to 'name'

#2-17
age=29
year=2020
print("age", age, "year", year)

#2-18
age=29
print("age", age)
age=10
print("age", age)


#2-19
age=29.5
first_name="John"
lastName = "Doe"
print ("Name", first_name, lastName)
print ("Age", age)
print("Data Type of 'lastName'", type(lastName)) 
print("Data Type of 'Age'", type(age))

#2-20
age=20
print("age =", age)
age="xyz"
print("age =", age)


#2-21
first_name = input('Enter your first name:')
lastName = input("Enter last name: ")
print("Hello", first_name, lastName)

#2-22
age = input("Enter age: ")
print ("Data Type of 'age' : ", type(age))    # try non-numeric input
age = int(age)
print ("Data Type of 'age' after 'int(age)' : ", type(age))
print ("age", age)


age = int(input("Enter age: ")) # match parentheses
income = float(input("Enter your income: "))
print ("age", age, "income", income)

#2-23
hourly_rate=16     # rate of $16 per hour
hours=20        # hours worked
bonus=3
salary = hourly_rate * hours + bonus
print ("salary", salary)

print(salary/hours)
print(salary//hours)

print ("5/2 =", 5/2, "    5//2 = ", 5//2, "     -5//2 =", -5//2)

#2-25
print ("5%2 = ", 5%2)  #returns the reminder instead of quotient

seconds = 500
print (seconds, "seconds = ", seconds // 60, "Minutes and ", seconds % 60, "Seconds")

#2-27
  
print ("2 * 5=", 2*5)
print ("2.0 * 5=", 2.0*5)  # Mixed-type expression - result is float

print (int(2.1))  # fractional part truncated

          
#2-30
print ('1'+'1')
print ('1' '1')
print(1+'1')

#2-34
print('One')
print('Two')
print('Three')

print('One', end= ' ') #space instead of newline
print('Two', end= ' ')
print('Three')

print('One', end= '')  #no spaces 
print('Two', end= '')
print('Three')

print('One', 'Two', 'Three')
print('One', 'Two', 'Three', sep='')  #no space as separator
print('One', 'Two', 'Three', sep='*') # '*' as separator

#2-35
print('One\nTwo\nThree')
print('One\tTwo\tThree')

#2-38 & 39
# This program demonstrates how a floating-point
# number can be rounded, and/or displayed as currency.
monthly_pay = 5250.29
annual_pay = monthly_pay * 12

print("Annual Pay without any formatting=$", annual_pay, "\n")

print("Annual Pay without any formatting=$", annual_pay, sep='', end='\n\n\n')

# f-string to format - rounded to 2 decimal places
print(f'Annual pay after rounding=${annual_pay:.2f}.\n')

# f-string - comma delimeter for currency and rounded to 2 
print(f'Annual pay after rounding and currency format=${annual_pay:,.2f}')

#2-41 & 42
# This program displays the following numbers
# in two columns.
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

#print without formatting
print('Numbers without formatting:')
print(num1, num2)
print(num3,num4)
print(num5,num6, '\n')

# Each number is displayed in a field of 15 spaces
# and rounded to 2 decimal places.
print('Numbers formatted with 15 spaces and rounded to 2 places:')
print(f'|{num1:15.2f}|{num2:15.2f}|')
print(f'|{num3:15.2f}|{num4:15.2f}|')
print(f'|{num5:15.2f}|{num6:15.2f}|\n')

# using Alignment designators <, ^, >
print('Numbers formatted with alignment:')
print(f'|{num1:<15.2f}|{num2:<15.2f}|   <Left-Aligned')
print(f'|{num3:^15.2f}|{num4:^15.2f}|   ^Center-Aligned')
print(f'|{num5:>15.2f}|{num6:>15.2f}|   >Right-Aligned')


#2-50 & 51
import turtle
turtle.forward(100)   # move forward 100 pixels
turtle.left(120)      # turn left 120 degrees
turtle.forward(100)

#2-59
import turtle
turtle.hideturtle()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.end_fill()
