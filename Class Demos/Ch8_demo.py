#8-5
# Accessing individual characters in a String
# first method using a for loop
name='Juliet'
print(name)
for ch in name:
    print(ch)
#-------------------------------------
# second example using a for loop
# This program counts the number of times the letter T
#  (uppercase or lowercase)appears in a string.

def main():
    # Create a variable to use to hold the count.
    # The variable must start with 0.
    count = 0
    
    my_string = input('Enter a sentence: ')  # Get a string

    for ch in my_string:    # Count the T/t's.
        if ch == 'T' or ch  == 't':
            count += 1

    # Print the result.
    print(f'The letter T/t appears {count} times.')

# Call the main function.
main()

#------------------------------------------------------------------
#8-6 - Accessing individual characters using Indexing

my_string='Roses are red'
print(my_string)
print('\nFirst character - my_string[0]   = ', my_string[0])
print('Seventh character - my_string[6] = ', my_string[6])

# use of negative indexes - right to left with -1 being last char
print('\nLast Character - my_string[-1]   = ', my_string[-1])
print('Second from last - my_string[-2] = ',my_string[-2])
print('13th from last - my_string[-13]  = ', my_string[-13])

#------------------------------------------------------------------
#8-7 - IndexError and use of len() function

city='Boston'
print('city = ', city)
index=0
while index < 7:       # IndexError at the last index
    print(f'city[{index}] = ', city[index])
    index += 1

# Avoiding IndexError with len() function
city='Boston'
print('\ncity = ', city)
index=0
while index < len(city): # IndexError avoided with len()
    print(f'city[{index}] = ', city[index])
    index += 1

#------------------------------------------------------------------
#8-8 String Concatenation

message = 'Hello ' + 'world'
print(message + '!')

letters = 'abc'
letters += 'def'   # same as letters=letters+'def'
print(letters)

#------------------------------------------------------------------
#8-9 String is Immutable (once created, cannot be changed)
friend='Bill'
print('friend = ', friend, '\nfriend[0] = ', friend[0])

# can we change the first character to J?
friend[0]='J'   # No - gives an error because of str being immutable

# We can create a new string and assign it to friend variable
friend='J'+friend[1:]  # remember slicing operator from Lists
print(friend)

#------------------------------------------------------------------
#8-11 Slicing a string
# REMEMBER Indexes start from ZERO
name='Patty Lynn Smith'
print('name=', name)

print('\nREMEMBER Indexes start from ZERO')
print('\nstarting from index 6 upto, but not including 10')
print('name[6:10]=', name[6:10])

print('\nstart index of zero - same as [0:5],not including 5')
print('name[:5]=', name[:5])

print('\nstart from index 11 upto length of str -same as [11:len(name)]')
print('name[11:]=', name[11:])  

print('\nthe entire string - same as [0:len(name)]')
print('name[:]=', name[:])   

print('\nwith a step value of 2 - same as in range()')
print('name[2:8:2]=', name[2:8:2])  

print('\nNegative index-starts from 5th from end-same as [-5:len(name)]')
print('name[-5:]=', name[-5:])  

# negative step changes the slice order from the tail
# goes from the last character to the first character
print('\nNegative Step changes the order in reverse - right to left')
print('name[::-1]=', name[::-1])

# -ve step changes the order from right to left
# starts from -2 and goes till beginning of string
print('\nright to left - starting from -2 till beginning of str')
print('name[-2::-1]=', name[-2::-1])

# -ve step - right to left -
# starts at -2 goes left till, but not including 1
print('\nright to left - starts from -2 till, but not including 1')
print('name[-2:1:-1]=', name[-2:1:-1]) 

#------------------------------------------------------------------
#8-12 use of 'in' operator
text = 'Four score and seven years ago'
if 'seven' in text:
    print('The string "seven" was found\n')
else:
    print('The string "seven" was not found\n')

# use of 'not in' operator
search_text = 'Five'
if search_text not in text:
    print('Search text not found')
else:
    print('Search text found')

#------------------------------------------------------------------
#8-14 String Testing Methods
# This program demonstrates several string testing methods.
def main():
    # Get a string from the user.
    user_string = input('Enter a string: ')

    print('This is what I found about that string:')
    
    # Test the string.
    if user_string.isalnum():
        print('The string is alphanumeric.')
    if user_string.isdigit():
        print('The string contains only digits.')
    if user_string.isalpha():
        print('The string contains only alphabetic characters.')
    if user_string.isspace():
        print('The string contains only whitespace characters.')
    if user_string.islower():
        print('The letters in the string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase.')

# Call the main function.
main()

#------------------------------------------------------------------
#8-16   String Modification methods
# upper() and lower() methods
letters="ABCD"
print("Original: ", letters, "\nletters.lower():", letters.lower())
input()

letters='wxyz'
print("\nOriginal: ", letters, "\nletters.upper():",  letters.upper())
input()

# strip(), lstrip() and rstrip() to remove whitespace characters
#       such as spaces, newlines(\n) and tabs(\t)
# we used rstrip('\n') in file reads...
text='   test   '
print('\nOriginal Text :|'+text+'|')
print('Strip leading and trailing : text.strip(): |'+text.strip()+'|')
print('Strip only leading : text.lstrip():|'+text.lstrip(),'|')
print('Strip only trailing: text.rstrip():|'+text.rstrip()+'|')

#------------------------------------------------------------------
#8-17  String Search Methods
# use of startswith() method
file_name=input('Enter the filename: ')
if file_name.endswith('.txt'):
    print('That is a text file')
elif file_name.endswith('.py'):
    print('That is a Python source file')
elif file_name.endswith('.doc'):
    print('That is a Word document file')
else:
    print('Unknown file type')

#-----------------------------------------------------
#8-18  Search methods
# use of find() method
text='Four score and seven years ago'
print(text)
position=text.find('score')
if position != -1:
    print('Word "score" was found at index ', position)
else:
    print('Word "score" was not found')
print()

# replace() method
text='Four score and seven years ago'
print(text)
new_text=text.replace('years', 'days')
print('Replaced text =', new_text)

#------------------------------------------------------------------
#8-22  Split() method

date_string = '11/26/2020'    # Create a string with a date
print("Original String:", date_string)
    
date_list = date_string.split('/')  # Split the date to create a list
print("List after string.split('/'):", date_list)
    
#------------------------------------------------------------------
#8-26
# This program reads test scores from a CSV file
# and calculates each student's test average.
''' Create a file 'test_scores.csv' with the content as below:
Jill,87,79,91,82,94
Pat,72,79,81,74,88
John,94,92,81,89,96
Smith,77,56,67,81,79
Will,79,82,85,81,90
'''
def main():
    csv_file = open('test_scores.csv', 'r') # Open the file.

    # Read the file's lines into a list.
    lines = csv_file.readlines()
    
    csv_file.close() # Close the file.

    print('Average Scores:')
    # Process the lines.
    for line in lines:
        # Get the test scores as tokens.
        tokens = line.split(',')
        
        # Calculate the total of the test scores.
        total = 0.0
        for score in tokens[1:]:  # ignore first names column
            total += float(score)
        
        # Calculate the average of the test scores.
        average = total / (len(tokens)-1)
        print(tokens[0], f': {average:.2f}')

# Execute the main function.
main()

#-----------------------------------------------------------
# P1
greeting = "Good Evening"

for char in greeting:
    if char == 'd':
        break
    print(char, end='')
else:      # else clause in for loop when no break occurs
            # similar to else clause in try/except
    print("Good Morning")

#-----------------------------------------------------------
# P2
text = 'Smith'
count = 0
while count < len(text):
    count += 1
print(count)

#------------------------------------------------------
#P3
def main():
    user_string = "ALPHA"    
    if user_string.isalnum():
        print('The string is alphanumeric.')
    elif user_string.isdigit():
        print('The string contains only digits.')
    elif user_string.isalpha():
        print('The string contains only alphabetic characters.')
    if user_string.isspace():
        print('The string contains only whitespace characters.')
    if user_string.islower():
        print('The letters in the string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase.')

# Call the main function.
main()

#------------------------

