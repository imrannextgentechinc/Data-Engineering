# Accept number of rows and columns as input
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

# Create the 2D array
array = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(i * j)
    array.append(row)

# Print the 2D array
print("Generated 2D Array:")
for row in array:
    print(row)
# Iterate through the rows