#List are the mutable datatype in Python
# Empty list can be created using built-in list() function
a = list() # This gives empty list 'a'
b = [] # Empty list can also be created in this way

c = [1, 2, 3] # This is a non-empty list

# List are hetrogeneous data type. That means it can have the elements of different data tyypes

c = [1, "Hello", [5, 6, 7], (1, 2)] # List with multiple date types
print c


# Accessing List elements
# List elements can be accessed with indexing and slicing
# List indexing starts from 0 for forward indexing and -1 for backward indexing

a = [1, "Hello", "World", 5.0, [4, 5,6], 5]
print(a[0]) # This gives 1
print(a[-1]) # negative index starts from -1. So, it gives 5

print(a[4]) # It gives [4, 5, 6]

print(a[4][1]) # It gives 5 from the nested list

print(a[6]) # This gives list index out of range error
print(a[-8]) # This also raises IndexError

# We can assign item in any particular index of a list
a[2] = 10 # This changes value at 2nd index of the list to 10

# Slicing in list
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[:]) # This gives exactly the same list
print(a[:6]) # This includes elements from 0 to 5, 6 is not included.Result [0, 1, 2, 3, 4, 5]
print(a[0:6]) # This is same as above [:6]
print(a[5:]) # This includes elements from 5th index to the last
# Result [5, 6, 7, 8, 9, 10]

print(a[1:8])
# This gives [1, 2, 3, 4, 5, 6, 7]
print(a[1:6:2]) # It jumps 1 step for elements from 1 to 7.

Negative Slicing
print(a[:-4]) # This gives elements from 0 index to -5th index [0, 1, 2, 3, 4, 5, 6]
print(a[-5:]) # It gives result from -5th index to the last element [6, 7, 8, 9, 10]
print(a[-6:-2]) # It gives elements from -6th index to -3rd index [5, 6, 7, 8]
print(a[-6:-8]) # This gives empty list []


# List operations Concatination with '+' operator
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a + b) # This concatenates two lists
# Result [1, 2, 3, 4, 5, 6, 7, 8]

# List operations with '*' operator (broadcast)
print(a*2) #It gives [1, 2, 3, 4, 1, 2, 3, 4]

#Membership Check
print(2 in a) # It True
print(5 not in b) # It gives False

# Operation

# Methods ---- a = [1, 2]
# Methods are tthe functions which are compulsarily called by and object
# a.append(3) -- we are calling the a list and then using the function --append need a (a. is a object here)
# 3 will be aaded to the existing list
# Built-in functions --- example ---print()  list()

#List Methods
a = [1, 2, 3]
a.append("hello")
print(a) # this gives [1, 2, 3, "hello"]

result = a.append(4)
#This statement appends value 4 to the list 'a' but it doesn't return anything (i.e None)

print(a)
# [1, 2, 3, "hello", 4]
print(result) #This gives None

a = [1, 2, 3]
b = [4, 5, 6]
c = a.extend(b)
print(c) #None
print(a) # result => [1, 2, 3, 4, 5, 6]
# Extend() method also returns none type


a.insert(1, "Hello World")
print(a) # result => [1, "Hello World", 2, 3]

a.remove(3) # This removes 3 from the list
print(a) #Result => [1, "Hello World", 2]
a.remove("hello World") # result => [1, 2]

#But if we pass the elements not present in the list to the remove method it raises error.








