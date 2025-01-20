# Function to check if all digits of a number are even
def all_even_digits(num):
    return all(int(digit) % 2 == 0 for digit in str(num))

# Iterate through numbers from 100 to 400 (inclusive)
for num in range(100, 401):
    if all_even_digits(num):
        print(num)
