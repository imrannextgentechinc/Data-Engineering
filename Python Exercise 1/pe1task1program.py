# Write a Program to find numbers divisible by 7 and multiples of 5 between 1500 and 2700

# List to store the result
result = []

# Loop through the range
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        result.append(num)

# Print the result
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700 are:", result)