#Write a Python program to find the index of an item in a tuple

# Sample tuple
my_tuple = (10, 20, 30, 40, 50)

# Item whose index you want to find
item = 30

# Finding the index of the item
try:
    index = my_tuple.index(item)
    print(f"The index of {item} is {index}")
except ValueError:
    print(f"{item} is not in the tuple")

