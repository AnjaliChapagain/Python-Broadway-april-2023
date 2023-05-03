# True and False are the keywords for Boolean type in python
# Logical operations, relational operations, identity and membership operations returns boolean result

a = 1
b = 2
c = 0

print(bool(a) and bool(b))  # This gives True
print (bool(a) and bool(c)) # False
print(bool(a) or bool(c)) # True

# Relational Operations
print(a > b) #False
print(b > a) # True
print(a == b) # false
print(a != b) # True

# Identity operations
a = 1
b = 1
c = 2
print(a is b) # True
print(a is c) # False

# Membership Operations
print(2 in [1, 2, 3]) # True
print(3 not in [1, 2, 3]) # false
print("h" in "hello") # True

# Boolean is a subclass of integer type in python.Thus True represents integer 1 and False represents 0.
# Arithmetic operations is possible for the Boolean type

print(True +1) # result => 2 (1 +1)
print(False + 5) # result=> 5 (0 + 5)
print (False * 70) # result -- 0 (0*70)

# bool() built-in function
# bool() function can take any object as a parameter and returns True or False
# based on the truthy or falsy nature of the object

# Any non-empty strings, Tuple, dictionary, set are truthy in nature.
# Also, all integers are truthy in nature except 0.
print(bool("Hello")) # true
print(bool({"name": "Jon"})) #True
print(bool({1, 2, 3})) # True
print(bool(5)) # True
print(bool(-5)) # True
print(bool(True)) # True

# All empty list, dictionary, set, string(or any empty object) are falsy in nature.
# 0 and None are also falsy in nature.
print(bool(None)) # False
print(bool(0)) # False
print(bool("")) # False
print(bool([])) # False
print(bool({})) # False
print(bool(False)) # False





