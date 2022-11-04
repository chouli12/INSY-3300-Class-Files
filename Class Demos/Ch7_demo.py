#7-5 / 6
# list of integers
even_numbers = [2,4,6,8,10]
print(type(even_numbers))
print(even_numbers)

input() # pause

# list of strings
names = ["Molly", "Steven", "Will", "Alicia", "Adriana"]

# list of different data types
info = ["Alicia", 27, 1550.87]

# can use print function to display list elements
print(even_numbers, names, info)

input()   # pause
# built-in list() function can convert
#    certain objects to lists
numbers = list(range(5))
print(numbers)

input()
numbers = list(range(1,10,2))
print(numbers)

input()
letters = list('John')
print(letters)

#-----------------------------------------------------------------
#7-7
# make five copies of list [0] and join together
numbers = [0] * 5  
print(numbers)

input()
# make three copies of a list and join together
numbers = [1,2,3] * 3
print(numbers)

input()
# iterate over a list with for loop
numbers = [1,2,3,4]
for num in numbers:
    print(num, num**2)  # print num and its squares

#-----------------------------------------------------------------
#7-8  Using Indexing
    
my_list=[10,20,30,40]
print(my_list)

input()
# use indexing to print second and fourth elements
#   indexing starts at zero
print("Second element =", my_list[1],
      "Fourth element =", my_list[3])

input()
# use negative indexing to print from last element
print("Last element =", my_list[-1],
      "Third element from last =", my_list[-3])

input()
# indexing error
# try accessing an element with invalid index
print(my_list[4])   

#-----------------------------------------------------------------
#7-9 Using len() function
my_list=[10,20,30,40]
size=len(my_list)  # lenght of the list
print(size)

input()
text='Pyhton' # string data type
print(len(text)) # len() function also works on str type

input()
#using len() function to prevent index error in a loop
index=0
while index<len(my_list): # loop till last list index
    print(my_list[index])
    index+=1
    
input()
# using len() along with range() function in a for loop
names = ["Molly", "Steven", "Will", "Alicia", "Adriana"]
for index in range(len(names)):
    print(names[index])

#-----------------------------------------------------------------
#7-10 Lists are mutable
    
my_list=[10,20,30,40]
print(my_list)

# change 3rd element of the list (mutable)
my_list[2]=99
print("\nList after the change: ", my_list)

#---------------------------------------------------
# Another example
# The NUM_DAYS constant holds the number of
# days that we will gather sales data for.
NUM_DAYS = 5

def main():
    # Create a list to hold the sales for each day.
    sales = [0] * NUM_DAYS
    print(sales)

    print('Enter the sales for each day.')
    
    # Get the sales for each day.
    for index in range(len(sales)):
        sales[index] = float(input(f'Day #{index + 1}: '))

    # Display the values entered.
    print('Here are the values you entered:')
    for value in sales:
        print(value)

# Call the main function.
main()

#-----------------------------------------------------------------
#7-11 List concatenation
list1=[1,2,3,4]
list2=[10,20,30]
list3=list1+list2
print("list1:", list1, "\nlist2:", list2,
      "\nlist3:", list3)

input()

list1+=list2    # same as list1=list1+list2
print("\nlist1:", list1)

input()
# invalid to concatenate a non-list to a list
list4=list1+40  

#-----------------------------------------------------------------
#7-12  Slicing a list
# REMEMBER Indexes start from ZERO
days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
print('days=', days)

print('\nREMEMBER Indexes start from ZERO')
print('\nstarting from index 2 upto, but not including 5')
print('days[2:5]=', days[2:5])
input()

print('\nstart index of zero - same as [0:6],not including 6')
print('days[:6]=', days[:6])
input()

print('\nstart from index 2 upto length of list-same as [2:len(days)]')
print('days[2:]=', days[2:])  
input()

print('\nthe entire list - same as [0:len(days)]')
print('days[:]=', days[:])   
input()

print('\nwith a step value of 2 - same as in range()')
print('days[1:6:2]=', days[1:6:2])  
input()

print('\nNegative index-starts from 5th from end-same as [-5:len(days)]')
print('days[-5:]=', days[-5:])  
input()

# negative step changes the slice order from the tail
# goes from the last element to the first element
print('\nNegative Step changes the order in reverse - right to left')
print('days[::-1]=', days[::-1])
input()

# -ve step changes the order from right to left
# starts from -2 and goes till beginning of list
print('\nright to left - starting from -2 till beginning of list')
print('days[-2::-1]=', days[-2::-1])
input()

# -ve step - right to left -
# starts at -2 goes left till, but not including 1
print('\nright to left - starts from -2 till, but not including 1')
print('days[-2:1:-1]=', days[-2:1:-1]) 

#-----------------------------------------------------------------
#7-13
# This program demonstrates the 'in' operator
def main():
    # Create a list of product numbers.
    prod_nums = ['V475', 'F987', 'Q143', 'R688']

    # Get a product number to search for.
    search = input('Enter a product number: ')

    # Determine whether the product number is in the list.
    if search in prod_nums:
        print(f'!!! {search} was found in the list.!!!')
    else:
        print(f' {search} was NOT found in the list.')

# Call the main function.
main()

#-----------------------------------------------------------------
#7-14 - Append method
# This program demonstrates how the append
# method can be used to add items to a list.
def main():
    name_list = []  # First, create an empty list.

    again = 'y'   # Create a variable to control the loop.
    
    while again == 'y':    # Add some names to the list.
        name = input('\nEnter a name: ')  # Get a name from the user.

        name_list.append(name)   # Append the name to the list.

        print('Do you want to add another name?') # Add another one?
        again = input('y = yes, anything else = no: ')

    print('\nHere are the names you entered.')  # Display the names 
    for name in name_list:
        print(name)
        
# Call the main function.
main()

#-----------------------------------------------------------------
#7-14 - Index method
# This program demonstrates how to get the index of an item
# in a list and then replace that item with a new item.
def main():
    food = ['Pizza', 'Burgers', 'Chips']  # Create a list with some items

    print('\nHere are the items in the food list:\n', food)

    item = input('\nWhich item should I change? ')  # Get the item to change.

    try:      
        item_index = food.index(item)  # Get the item's index in the list.

        # Get the value to replace it with.
        new_item = input('Enter the new value: ')

        food[item_index] = new_item   # Replace the old item with the new

        print('\nHere is the revised list:\n', food)
    except ValueError:
        print('\nItem ' + item + ' was not found in the list.')
        
# Call the main function.
main()

#-----------------------------------------------------------------
#7-14, 15 & 16 - list methods
print("List Methods Illustration")
list1=[5,1,"Jill",3,0]
print("\nOriginal List (list1): ", list1)

list1.append("Jim")
print("\nList after list1.append('Jim'): ", list1)
input()

print("\nlist1.index('Jill'): ", list1.index("Jill"))
input()

list1.insert(2,10)
print("\nList after list1.insert(2,10): ", list1)
input()

list2=["Jill", "Sam", "Will", "Matt"]
print("\nOriginal List (list2): ", list2)
list2.sort()   # sort list2 using sort() method
print("\nSorted list after list2.sort(): ", list2)
input()

list2.sort(reverse=True)   # optional reverse parameter
print("\nlist2.sort(reverse=True): ", list2)
input()

list3=[5,1,4,1,3,0]
print("\nOriginal List (list3): ", list3)
list3.reverse()
print("\nReversed List after list3.reverse(): ", list3)
input()

list3.remove(1) # remove first occurrence of '1'
print("\nlist3.remove(1): ", list3)


#-----------------------------------------------------------------
#7-17 - del statement and built-in functions

# use of del statement
list1=[1,2,3,4,5]
print("\nOriginal List: ", list1)
del list1[2]   # remove third item
print("After deletion: ", list1)

#min() and max() functions
list2=[5,11,3,61,4,32]
print("\nList Values: ", list2)
print("The lowest value is ", min(list2))
print("The highest value is ", max(list2))

#-----------------------------------------------------------------
#7-32 Tuples
# enclose the elements of a tuple in parantheses
my_tuple=(1,2,3,4,5)
print(my_tuple, '\n')

# a sequence without parantheses also creates a tuple
a=1,2,3,5    # creates variable a as a tuple
print(type(a))
print(a)

a=1,     # creates a tuple with one element
print(a)

#-----------------------------
# iterate a tuple with a for loop exactly as with a list
names = ("Molly", "Steven", "Will", "Alicia", "Adriana")
print(names)
for n in names:
    print(n)
print()

# iterate a string with a for loop exactly as with a list and tuple
name="Molly"
print(name)
for n in name:
    print(n)

#-----------------------------------------------------------------------
#7-33
# make three copies of a tuple and join together
numbers = (1,2,3) * 3
print("(1,2,3) * 3 = ", numbers)

input()
# use of + operator
tuple1=(1,2,3)
tuple2=(10,20,30)
print("\ntuple1=",tuple1,"\ntuple2=",tuple2)
tuple1+=tuple2
print('tuple1+tuple2=', tuple1)

input()
# 'in' operator
names = ("Molly", "Steven", "Will", "Alicia", "Adriana")
name="Will"
if name in names:
    print (name, "is in ", names)
else:
    print (name, "is NOT in ", names)

input()
# in operator works for Strings as well
full_name="Will Smith Junior"
search_str="Smith"
if search_str in full_name:
    print (search_str, "is found in ", full_name)
else:
    print (search_str, "is NOT found in ", full_name)
    
#------------------------------------------------------
# like Lists, Tuples and Strings support indexing
print('Like Lists, Tuples and Strings support indexing')
names = ("Molly", "Steven", "Will", "Alicia", "Adriana")
print('names: ', names, '\nnames[2]:', names[2], ' names[4]:', names[4])

input()
name="William Smith"
print('\nname: ', name, '\nname[2]:', name[2], 'name[4]:', name[4])
input()

# Tuples and Strings support slicing same as lists
print('\nLike Lists, Tuples and Strings support slicing')
print('\nnames[1:4]', names[1:4])  # starting from index 1 upto, but not including 3
print('\nname[1:4]', name[1:4])
input()

# Tuples and Strings support len(), min() and max() functions
print('\nLike Lists, Tuples and Strings'+
      ' support len(),min() and max() functions')
print('\nlen(names): ', len(names),
      'min(names)=', min(names), ' max(names)=', max(names))

print('\nlen(name): ', len(name),
      'min(name)=', min(name), ' max(name)=', max(name))
input()

# Like Lists, Tuples and Strings support index method
print('\nLike Lists, Tuples and Strings support index method')
print("\nnames.index('Will'): ", names.index("Will"))
print("\nname.index('a'): ", name.index('a'))


#---------------------------------------------------------------
#7-34 - Immutable
names = ("Molly", "Steven", "Will", "Alicia", "Adriana")
print(names[2])
names[2]="Smith" # will cause an error due to immutable nature

input()
# Strings are also immutable
name="Steven"
print(name[2])
name[2]='x' # will fail due to immutable nature

input()
# will work with a list as it is mutable
names = ["Molly", "Steven", "Will", "Alicia", "Adriana"]
print (names)
names[2]="Smith"
print(names)


#---------------------------------------------------------------
#7-35
# convertion between lists and tuples
tuple1=(20,10,30,90)
print('tuple=', tuple1)
# list() function to convert tuple to list
list1=list(tuple1)  
print('tuple converted to list=',list1)

input()

list2=['sun','mon','tue','wed']
# use of tuple() function to convert list to tuple
tuple2=tuple(list2)
print('\nlist=', list2)
print('list converted to tuple=',tuple2)

# ----------------------------------------------------------
# P1
tup1=(1,2)
tup2=(3,4)
for i in tup1:
    for j in tup2:
        print(i,j)

#-------------------------------------------
# P2
def myfunc(lst1):
    lst2=lst1
    return [1,2]

lstX = [1,2,3,4,5]
lstY = myfunc(lstX)
print(lstY)

#---------------------------------------------


