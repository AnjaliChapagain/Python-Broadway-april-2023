### Mutable and Immutable ###
# Mutable objects are those objects whose value can be changed even after it's creation

# Immutable objects are those objects whose value can't be changed once it is created

# Integer, Boolean, Float, Tuple, Strings are immutable datatypes in python
# List , Dictionary and set are the mutable datetypes

a =(1, 2, 3) # Immutable type
b = [1, 2, 3] # Mutable type
b[1] = 5 # This is possible as list is a mutable type
print(b)
# a[1] = 5 # This is not possible


