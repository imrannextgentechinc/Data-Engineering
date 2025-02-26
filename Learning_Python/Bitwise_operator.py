
#Bitwise operators in Python are used to perform bit-level operations on integers. 
# These operators treat numbers as a sequence of bits (binary) and operate on them bit by bit. Here are the common bitwise operators in Python:

#AND (&): Sets each bit to 1 if both bits are 1.
#OR (|): Sets each bit to 1 if one of the bits is 1.
#XOR (^): Sets each bit to 1 if only one of the bits is 1.
#NOT (~): Inverts all the bits.
#Left Shift (<<): Shifts bits to the left by a specified number of positions.
#Right Shift (>>): Shifts bits to the right by a specified number of positions.
#Here are some examples to illustrate these operators:


# Bitwise AND
a = 5  # (binary: 0101)
b = 3  # (binary: 0011)
result_and = a & b  # (binary: 0001) -> 1
print(f"Bitwise AND: {a} & {b} = {result_and}")

# Bitwise OR
result_or = a | b  # (binary: 0111) -> 7
print(f"Bitwise OR: {a} | {b} = {result_or}")

# Bitwise XOR
result_xor = a ^ b  # (binary: 0110) -> 6
print(f"Bitwise XOR: {a} ^ {b} = {result_xor}")

# Bitwise NOT
result_not = ~a  # (binary: 1010) -> -6 (in 2's complement form)
print(f"Bitwise NOT: ~{a} = {result_not}")

# Left Shift
shift_left = a << 1  # (binary: 1010) -> 10
print(f"Left Shift: {a} << 1 = {shift_left}")

# Right Shift
shift_right = a >> 1  # (binary: 0010) -> 2
print(f"Right Shift: {a} >> 1 = {shift_right}")


#Explanation:
#Bitwise AND (&): 5 & 3 results in 1 because only the last bit is 1 in both numbers.
#Bitwise OR (|): 5 | 3 results in 7 because at least one bit is 1 in each position.
#Bitwise XOR (^): 5 ^ 3 results in 6 because the bits differ in the second and third positions.
#Bitwise NOT (~): ~5 results in -6 because it inverts all bits and represents the result in two's complement form.
#Left Shift (<<): 5 << 1 results in 10 because it shifts all bits to the left by one position, adding a 0 at the end.
#Right Shift (>>): 5 >> 1 results in 2 because it shifts all bits to the right by one position, discarding the last bit.
#These operations are useful in various low-level programming tasks, such as setting, clearing, and toggling specific bits in a number.