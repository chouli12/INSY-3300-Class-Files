#9-4
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}

print(type(phonebook))
print(phonebook)

#---------------------------------------------------------
# 9-5 - Retrieving a value
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}

print('Phone# for John:', phonebook['John'])
print('Phone# for Katie:', phonebook['Katie'])

# Try a key not in the dictionary
print('Jim:', phonebook['Jim'])  

'''
# using 'in' operator
if 'Jim' in phonebook:
    print(phonebook['Jim'])
else:
    print('Jim is not in phonebook')
'''
#-------------------------------------------------------------
# 9-6 - Adding or updating elements
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}
print("original phonebook:\n", phonebook)

# add a new entry
phonebook['Joe'] = '972-8759'
print('\nAfter adding Joe:\n', phonebook)

#update an existing entry
phonebook['John'] = '972-8944'
print('\nAfter updating John:\n', phonebook)

#-------------------------------------------------------------
# 9-7  Deleting an element
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}
print("original phonebook:\n", phonebook)

# Delete a key-value pair
del phonebook['Chris']
print('\nAfter deleting Chris:\n', phonebook)
print()

# try deleting Chris again
del phonebook['Chris']

'''
# del for Lists

list1=[1,2,3,4,5]
print("\nOriginal List: ", list1)
del list1[2]   # remove third item
print("After deletion: ", list1)
'''

#----------------------------------------------------------------
#9-8 len function
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}
print("original phonebook:\n", phonebook)

print('No of elements:', len(phonebook))

#9-8 len function
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}
print("original phonebook:\n", phonebook)

print('No of elements:', len(phonebook))

# example of mixed data type values
employee={'name':'Kevin Kelley', 'id':12345, 'payrate':25.45}
print('\nemployee:', employee, "\nemployee['id']:", employee['id'])

#----------------------------------------------------------------
#9-9 Create an empty dictionary - can use either method below
phonebook={}
phonebook = dict()   # use of dict() function

phonebook['Chris']='393-4499'
phonebook['John']='393-2245'

print(phonebook)
'''
print("\nUse of for loop:")

# use of for loop
for key in phonebook:
    print(key, phonebook[key])
'''
#----------------------------------------------------------------
#9-10 Dictionary methods
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}
print('Original phonebook:\n', phonebook)
      
phonebook.clear()  # delete all the elements
print("\nphonebook after phonebook.clear():\n", phonebook)

print()
'''
# get method
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}

print(phonebook['Jim'])

print(phonebook.get('Jim', 'Jim not found'))
'''
#----------------------------------------------------------------
#9-11 Dictionary methods
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}
print('Original phonebook:\n', phonebook)
print()   

# using items() method
dv=phonebook.items()
print(dv)


# using for loop with items() method
print("\nUse of for loop with items() method:")

for key, value in phonebook.items():
    print(key, value)

'''
print()
for key in phonebook:
    print(key, phonebook[key])
'''
#----------------------------------------------------------------
#9-12 Dictionary methods
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}
print('Original phonebook:\n', phonebook)
print()

print(phonebook.keys())   #keys() returns a sequence of keys

# using for loop with keys() method
print()
for key in phonebook.keys():
    print(key)

#--------------------------------------
# using values() method
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}
print('\nOriginal phonebook:\n', phonebook)
print()

print(phonebook.values())   #values() returns a sequence of values

# using for loop with values() method
print()
for value in phonebook.values():
    print(value)

#----------------------------------------------------------------
# 9-13 - using pop method

phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}
print('Original phonebook:\n', phonebook)

print('\nUse of pop method to remove a key-value for "John":')
phone_num=phonebook.pop('John', 'John not found')
print(phone_num)
print('phonebook after pop:\n', phonebook)
print()

phone_num=phonebook.pop('John', 'John not found\n')
print(phone_num)
print('phonebook after pop:\n', phonebook)

#----------------------
# using popitem() method
phonebook={'Chris':'393-4499', 'John':'393-2245', 'Katie':'393-8745'}
print('Original phonebook:\n', phonebook)
print()

# popitem() to remove last dict element
name, phone_num=phonebook.popitem()
print(name, phone_num)
print('phonebook after popitem():\n', phonebook)
print()

name, phone_num=phonebook.popitem()
print(name, phone_num)
print('phonebook after popitem():\n', phonebook)
print()
'''
print(phonebook.popitem())
print(phonebook.popitem())
'''

#---------------------------------------------------------------

#9-22 Sets
myset=set()  # create an empty set

myset=set([100,2,3,400,5,6,100,400])  # list as an argument
print(myset)   #look for unordered and uniqueness
print()

'''
myset=set('Kelley')  # string as an argument
print(myset)

myset=set(('jim','john','chris', 'joe', 'jim'))  # tuple as an argument
print(myset)
print()

# creating a set with Curly Braces! Beware - can't create an empty set
s={1,100,10,2}
print(s)
'''
#---------------------------------------------------------------
#9-23 Set methods

myset=set([100,2,3,400,5,6,100,400])  # list as an argument
print('length of myset:', len(myset))   # len() method
print()

'''
# adding single element
myset=set()  # create an empty set
myset.add(10)
myset.add(100)
myset.add(2)
print(myset)
print()

myset.add(100)  #add duplicate does not raise an exception
print(myset)
print()

# adding a group of elements
myset=set([10,100,20])
print("myset before update:", myset)
myset.update([4,5,6,10,100], 'jim')
print(myset)
'''


#---------------------------------------------------------------
#9-24 Set methods
myset=set([100,2,3,400,5,6])  
print("Original myset: ", myset)  

# remove an element
myset.remove(2)
print("myset after removing 2: ", myset)

'''
myset.discard(100)  
print("myset after removing 100: ", myset)

myset.discard(200)   # does not raise an error

myset.remove(200)   # will raise an error

myset.clear()
print(myset)
'''
#---------------------------------------------------------------
#9-25 use of for loop and in operator
myset=set([100,2,3,400,5,6])
print("myset: ", myset)
for val in myset:
    print(val)
    
'''
# in operator
if 400 in myset:
    print('\nThe value 400 is in the set')
'''  

#---------------------------------------------------------------
#9-26 Union of sets
set1=set([1,2,3,4])
set2=set([3,4,5,6])
print("set1:", set1, " set2:", set2)

set3=set1.union(set2)
print("\nset1.union(set2): ", set3)

# use of | operator
set3=set1 | set2
print("\nset1 | set2: ", set3)
    
#---------------------------------------------------------------
#9-27 Intersection of sets
set1=set([1,2,3,4])
set2=set([3,4,5,6])
print("set1:", set1, " set2:", set2)

set3=set1.intersection(set2)
print("\nset1.intersection(set2): ", set3)

# use of & operator
set3=set1 & set2
print("\nset1 & set2: ", set3)
    
#---------------------------------------------------------------
#9-28 Difference of sets
set1=set([1,2,3,4])
set2=set([3,4,5,6])
print("set1:", set1, " set2:", set2)

set3=set1.difference(set2)
print("\nset1.difference(set2): ", set3)

# use of - operator
set3=set1 - set2
print("\nset1 - set2: ", set3)
    
#---------------------------------------------------------------
#9-29 Symmetrix Difference of sets
set1=set([1,2,3,4])
set2=set([3,4,5,6])
print("set1:", set1, " set2:", set2)

set3=set1.symmetric_difference(set2)
print("\nset1.symmetric_difference(set2): ", set3)

# use of ^ operator
set3=set1 ^ set2
print("\nset1 ^ set2: ", set3)
    
#---------------------------------------------------------------
#9-30/31 Subsets and Supersets
set1=set([1,2,3,4])
set2=set([2,3])
print("set1:", set1, " set2:", set2)

print("\nset2.issubset(set1): ", set2.issubset(set1))

print("\nset2<=set1:", set2<=set1)

print("\nset1.issuperset(set2): ", set1.issuperset(set2))

print("\nset1>=set2:", set1>=set2)

#---------------------------------------------------------------
