#9.	Write a function to swap the numbers without using a third variable
def swap_numbers(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Example usage
num1 = 5
num2 = 10
num1, num2 = swap_numbers(num1, num2)
print("After swapping:")
print("num1 =", num1)
print("num2 =", num2)


#explanation:
#This function takes two numbers as input and swaps them without using a third variable.
#It uses arithmetic operations to achieve the swap.
#The function returns the swapped values.
#The example usage demonstrates how to call the function and print the swapped values.