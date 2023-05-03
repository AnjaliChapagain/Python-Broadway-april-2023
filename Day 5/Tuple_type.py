# Tuple datatypes are similar to python list type but they are immutable
# Indexing and Slicing in tuple are same as that of list
# Empty tuple can be created using paranthesis () or tuple() built-in fuction

t = tuple() # An empty tuple
print(t)
t = (1, 2, 3) # A non empty tuple
print(t)
t = tuple([1, 2, 3]) # Tuple() function takes iterable  as a parameter

# Creating a tuple with single element
t = (1) # This seems like a tuple but, it is an integer type
print(type(t)) # Int
t = (1, ) # We need to add a comma while creating tuple with single element
print(type(t)) # Tup



# Tuple packing and unpacking
t = 1, 2, "Hello World" # A tuple can be created without using paranthesis as given in this example.
# This type of tuple creating is tuple packing

# Assigning of each tuple elements to individual variables in the LHS is called tuple unpacking
a, b, c = 1, 2, "Hello World"
print(a) # Result => 1
print(b) # result => 2
print(c) # Result => 2


# This is how we do swapping normally in other languages. With the use of third variable (c)
a = 1
b = 2

c = a
a = b
b = c

# Swapping can be implemented easily in Python with tuple packing and unpacking
a = 1
b = 2
a, b = b, a # Swapping using tuple packing/unpacking
print(a)
print(b)


# Elements in LHS must be equal to RHS in tuple packing and unpacking else it raises an error
a, b = 1, 2, 3 # This raises an error
# a, b, c = 1, 2 # This also raises an error



# Indexing and slicing in tuple is same as that of list

a = (1, 2, 3, 4, 5, 6, 7)
a[::2] # This traverse from forward jumping one step
# Result => (1, 3, 5, 7)

print(a[-2:-6:-1]) # Providing negative step size traverse the sequence from backward.
# Result => (6, 5, 4, 3)

print(a[::-1]) # This reverses the sequence. result => (7, 6, 5, 4, 3, 2, 1)


del a # This deletes the tuple a (del keyword deletes any object)



