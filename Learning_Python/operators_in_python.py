
#Unary operators are operators that operate on a single operand. They perform various operations such as negation, increment, and decrement. In Python, common unary operators include:

#Unary Plus (+): Indicates a positive value (usually redundant).
#Unary Minus (-): Negates the value of the operand.
#Logical NOT (not): Inverts the boolean value of the operand.
#Bitwise NOT (~): Inverts all the bits of the operand.
#Here are examples of each:

# Unary Plus
a = 5
print(+a)  # Output: 5

# Unary Minus
b = 5
print(-b)  # Output: -5

# Logical NOT
c = True
print(not c)  # Output: False

# Bitwise NOT
d = 5  # Binary: 0101
print(~d)  # Output: -6 (Binary: ...11111010 in two's complement)


# Relational operators are used to compare the values of two operands. 
# They return a boolean value (True or False) based on the comparison. Common relational operators in Python include:

# Equal to (==): Checks if the values of two operands are equal.
# Not equal to (!=): Checks if the values of two operands are not equal.
# Greater than (>): Checks if the value of the left operand is greater than the value of the right operand.
# Less than (<): Checks if the value of the left operand is less than the value of the right operand.
# Greater than or equal to (>=): Checks if the value of the left operand is greater than or equal to the value of the right operand.
# Less than or equal to (<=): Checks if the value of the left operand is less than or equal to the value of the right operand.

# Here are examples of each:

x = 10
y = 5

# Equal to
print(x == y)  # Output: False

# Not equal to
print(x != y)  # Output: True

# Greater than
print(x > y)  # Output: True

# Less than
print(x < y)  # Output: False

# Greater than or equal to
print(x >= y)  # Output: True

# Less than or equal to
print(x <= y)  # Output: False



# Logical operators are used to combine conditional statements. 
# They return a boolean value (True or False) based on the logic of the operands. Common logical operators in Python include:

# Logical AND (and): Returns True if both operands are true.
# Logical OR (or): Returns True if at least one of the operands is true.
# Logical NOT (not): Inverts the boolean value of the operand.

# Here are examples of each:

p = True
q = False

# Logical AND
print(p and q)  # Output: False

# Logical OR
print(p or q)  # Output: True

# Logical NOT
print(not p)  # Output: False



#Here is how we use = eqaual to assign the value to the variable that is known as assignment operator.

x = 2
y = 3

#Trying Arithematic operations

print(x+y)
print(x-y)
print(x*y)
print(x/y)

#We can also do 

x = x+2
print(x)

#we can also do this in another method as 
x += 2 # here by using += we are adding the value 2 to x
print(x)


#same as for multiplication 
x *= 2
print(x)

#same for substraction 
x -= 2
print(x)

#same for division
x /= 2
print(x)


#Lets try assigning values to two variables in one line with assignment operator
a,b = 5,6

print(a)
print(b)








