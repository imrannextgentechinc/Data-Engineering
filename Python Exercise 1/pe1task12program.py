#Write a  Python program to sum all the items in a list. Using both loop and sum function.

# lets take a Sample list
my_list = [1, 2, 3, 4, 5]

# Using a loop to sum the items
total = 0
for item in my_list:
    total += item

print("Sum using loop:", total)

# Using sum() function to sum the items
total_sum = sum(my_list)
print("Sum using sum() function:", total_sum)
