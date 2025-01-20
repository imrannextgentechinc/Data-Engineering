# Initialize the first two numbers of the Fibonacci series
a, b = 0, 1

# Print the Fibonacci series up to 50
print("Fibonacci series between 0 and 50:")

while a <= 50:
    print(a, end=" ")
    # Update the values of a and b to the next Fibonacci numbers
    a, b = b, a + b