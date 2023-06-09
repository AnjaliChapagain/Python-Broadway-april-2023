### Arithmetic Operators

# Addition
a = 1
b = 2
print(a + b)  # Here + is an addition operator

# Subtraction
a = 5
b = 2
print(b - a)  # Here - is a subtraction operator

# Multiplication
print(a * b)  # * operator is used for multiplication

# Division
print(a / b)  # / operator is used for division operation

# Exponent
print(a ** 2)  # This is 'a' raised to the power 2.
# ** is used for exponential operation.

print(a % 2)  # Here a is 5. So, remainder of 5/2 is 1.

print(a//2)  # Here // is an operator for floor division that terminated the decimal digits.




# Relational Operators
a = 1
b = 1
print(a == b)  # '==' is a comparision operator to check whether values are equal or not. Here it gives True

a = 5
print(a > b) # It returns False
print(b > a) # It returns True

a = 2
b = 2
print (a >= b) #It gives True
print(a <= b) #It gives False

print( a !=b ) # It gives False


# Logical Operations
# And
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

#Or
print(True and True) # True
print(True and False) # True
print(False and True) # True
print(False and False) # False

#Not
print(not True) #False
print(not False) #True

# Identity Operators
# is and is not are the identity check operators

a = 1
b = 1
# Here a and b both refers to the same object with value 1
print(a is b) # So it returns True

b = 123
print(a is b) # It returns False because b is another object with value 123
print(a is not b) # It gives True

#Membership Operator
ages =[21, 22, 23, 24]
print(21 in ages) # It gives True
print(22 not in ages) # It gives False

print( 25 in ages) # It gives False
print(25 not in ages) # It gives True

name = "broadway"
print('b' in name) # It gives True

#Assignment Operators

a = 1 # "=" is the simplest assignment operator which assigns value from the RHS to the variable on the LHS
a = a + 1 # This increases the value of a by 1 but this logic can also be written as following
a += 1 # Here += is an assignment operator

# Precedence and associativity
# Preceden e is the rule that determines the priority of operators in and operation

# Associativity is the rule that determines the priority of operators if one or more operators have the same precedence

# Normally Associativity is from left to right. But for ** operator it is from right to left

print(2**3**2) # 3**2 is evaluated first and the result is raised power to 2.










