a = "Hello World"
print(len(a)) # Returns the length of a sequence / iterable

print(bool(a)) # here a is a non-empty string which is truthy
# so it gives True

print(a[slice(1, 5)]) # slice() function can be used in the string slicing.
# First parameter is start and second is stop slice(start, stop, step)
# step can also be provided as the third parameter

print(type(a)) # This returns type of object inside the fxn
# Here it is string

