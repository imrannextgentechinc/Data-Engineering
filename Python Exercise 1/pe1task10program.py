#Write a Python program to create the multiplication table (from 1 to 10) of a number.

# Accept the number from the user
number = int(input("Enter a number: "))

# Create the multiplication table for the number
print(f"Multiplication table for {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
