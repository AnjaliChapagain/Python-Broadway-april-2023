# There are two types of copy for Python Objects
# Shallow copy
# Deep copy

a = [1, 2, 3]
b = a # This increased the reference count of [1, 2, 3]. But it is not actual copy
b.append(4)
print(b)
print(a)
# This appends the value 4 in both a and b because they both refer to the same object [1, 2, 3]

b = a.copy() # This makes a shallow copy of 'a' and assigns it to 'b'

# Now if we append a vlaue to 'b', then it doesn't change 'a'
b.append(5)
print(b)
print(a)

# But the case is quite different if a list has a mutable object as an element
a = [[1, 2, 3], 4]
b = a.copy()
b[0][1] = 5
print(b) # Result => [[1, 5, 3], 4]

# But this also changes the value in variable 'a' even if 'b' is the copy of 'a'
print(a) # Result => [[1, 5, 3], 4]
# This happened because b is only a shallow copy of 'a'.
# To overcome this, we should use deepcopy

from copy import deepcopy
b = deepcopy(a)
b[0][1] = 2
print(b) # result => [[1, 2, 3], 4}
print(a) # This doesn't change value in variable 'a'. Result => [[1, 4, 3], 4]

