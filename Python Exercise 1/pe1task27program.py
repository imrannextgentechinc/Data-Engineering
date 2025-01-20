#Write a  Python program to compute the element-wise sum of given tuples

# Original tuples
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)

# Computing the element-wise sum of the tuples
elementwise_sum = tuple(sum(x) for x in zip(tuple1, tuple2, tuple3))

# Printing the result
print("Element-wise sum of the said tuples:", elementwise_sum)

