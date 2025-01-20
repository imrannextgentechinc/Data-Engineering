# Ask the user for the number of rows
num_rows = int(input("Enter the number of rows: "))

# Construct the pattern using nested for loops
for i in range(1, num_rows + 1):
    for j in range(i):
        print("*", end=" ")  # Print "*" without moving to a new line
    print()  # Move to the next line after each row
