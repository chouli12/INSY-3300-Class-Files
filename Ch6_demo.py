# 6-10 & 12 & 13
# This program writes three lines of data to a file.
def main():
    # Open a file named philosophers.txt
    #   for write "w" ("a" for append) - create a file object
    # The file name directory convention is for Mac.
    #      Rewrite file directory for Windows 
    outfile=open('/Users/ravibadrachalam/Documents/philosophers.txt','w')

    # Write the names of three philosphers to the file.
    # newline is added at the end of line
    outfile.write('John Locke\n')  
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    outfile.close()   # Close the file

# Call the main function.
main()

#-----------------------------------------------------------------------------
#6-14
# This program reads and displays the contents of the philosophers.txt file.
def main():
    
    infile = open('/Users/ravibadrachalam/Documents/philosophers.txt', 'r')  # Open the file for reading
    
    file_contents = infile.read()   # Read the entire file's contents

    infile.close()      # Close the file

    print(file_contents)   # Print the data that was read into memory

# Call the main function.
main()

#-----------------------------------------------------------------------------
#6-14 to 17 - Read using while loop
# This program reads the contents of the file one line at a time.
def main():
    
    infile = open('/Users/ravibadrachalam/Documents/philosophers.txt', 'r') # Open a file for reading

    # Read first line from the file
    line = infile.readline()  

    while line != '':   # empty string indicates end of file
        # strip the newline '\n' from the string
        # try commenting this line to see output
        line = line.rstrip('\n')    
        print(line)
        line = infile.readline()  # read next line
        
    infile.close()  # Close the file

# Call the main function.
main()

#-----------------------------------------------------------------------------
#6-18  - Read using for loop
# This program reads the contents of the file one line at a time.
def main():
    
    infile = open('/Users/ravibadrachalam/Documents/philosophers.txt', 'r')  # Open the file for reading

    for line in infile:
        # strip the newline '\n' from the string
        line = line.rstrip('\n')    # try commenting this line to see output
        print(line)
        
    # Close the file.
    infile.close()

# Call the main function.
main()

#-----------------------------------------------------------------------------
#6-19
# This program demonstrates how numbers must be converted
#   to strings before they are written to a text file.

def main():
    
    outfile = open('/Users/ravibadrachalam/Documents/numbers.txt', 'w')  # Try "a" for append

    # Get name, age and salary from the user
    name = input('Enter name: ')
    age = int(input('Enter age (integer): '))
    salary = float(input('Enter salary (float): '))

    # Write the numbers to the file.
    outfile.write(name + '\n')
    outfile.write(str(age) + '\n')     # convert to string
    outfile.write(str(salary) + '\n')  # convert to string

    # Close the file.
    outfile.close()
    print('Data written to numbers.txt')

# Call the main function.
main()

#-----------------------------------------------------------------------------
#6-19
# This program uses the while loop to read
#    all of the values in the numbers.txt file.

def main():
    # Open the sales.txt file for reading.
    infile = open('/Users/ravibadrachalam/Documents/numbers.txt', 'r')

    # Read first line which is name
    name = infile.readline()

    while name != '':
        name = name.rstrip('\n')  #strip the newline '\n' from the string
        age = int(infile.readline())
        salary = float(infile.readline())
        print("Name :", name)
        print("Age :", age)
        print(f'Salary : {salary:.2f}\n')
        # read next line that happens to be name
        name = infile.readline()   
    
    # Close the file.
    infile.close()

# Call the main function.
main()

#-----------------------------------------------------------------------------
#6-19 alternate version using for loop
#  but it cannot distinguish name, age and salary
def main():
    # Open the sales.txt file for reading.
    infile = open('/Users/ravibadrachalam/Documents/numbers.txt', 'r')

    for line in infile:
        print(line.rstrip('\n'))
    
    # Close the file.
    infile.close()

# Call the main function.
main()

#-----------------------------------------------------------------------------
#6-22
# This program divides a number by another number.
def main():
    # Get two numbers.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    # try entering zero for num2

    # Divide num1 by num2 and display the result.
    result = num1 / num2
    print(f'{num1} divided by {num2} is {result}')

# Call the main function.
main()

#-----------------------------------------------------------------------------
#6-23
# This program divides a number by another number.
def main():
    # Get two numbers.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    # If num2 is not zero, divide num1 by num2
    if num2 != 0:     
        result = num1 / num2
        print(f'{num1} divided by {num2} is {result}')
    else:
        print('Cannot divide by zero.')
          
main()

#-----------------------------------------------------------------------------
#6-24
# This program divides a number by another number.
def main():
    try:
        # Get two numbers.
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))

        # Divide num1 by num2 and display the result.
        result = num1 / num2
        print(f'{num1} divided by {num2} is {result}')
        
    except ZeroDivisionError:
        print("ERROR: Cannot divide by zero")
        
# Call the main function.
main()

#-----------------------------------------------------------------------------
#6-26 /27
# This program divides a number by another number.
def main():
    try:
        # Get two numbers.
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))

        # Divide num1 by num2 and display the result.
        result = num1 / num2
        print(f'{num1} divided by {num2} is {result}')
        
    except ZeroDivisionError:      # comment for default except clause
        print("ERROR: Cannot divide by zero")
    except ValueError as err:      # comment for default except clause
        print("ERROR: Inputs must be valid numbers")
        print(err)
    except Exception as err:
        print(err)
        
# Call the main function.
main()

#-----------------------------------------------------------------------------
#6-28 and 29
# This program divides a number by another number.
def main():
    try:
        # Get two numbers.
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))

        # Divide num1 by num2 and display the result.
        result = num1 / num2
        
    except Exception as err:
        print(err)
    else:
        print(f'{num1} divided by {num2} is {result}')
    finally:
        print("END OF PROGRAM")
        
# Call the main function.
main()





