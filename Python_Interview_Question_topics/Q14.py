#How do you find the average of numbers in a list?

# There are multiple ways to find the average of numbers in a list. Here are two methods to do this:

# Method 1: Using the sum() and len() functions

def average(lst):
    return sum(lst) / len(lst)

print(average([1, 2, 3, 4, 5])) 


#Explanation:
# The average of a list of numbers is calculated by dividing the sum of the numbers by the total number of elements in the list.
# The sum() function is used to calculate the sum of all the numbers in the list.
# The len() function is used to calculate the total number of elements in the list.
# The average of the numbers is then calculated by dividing the sum by the total number of elements in the list.



# Method 2: Using a for loop
def average(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst) 

print(average([1, 2, 3, 4, 5]))

#Explanation:
# This method calculates the average of numbers in a list using a for loop.
# The total variable is initialized to 0.
# The for loop iterates over each element in the list and adds it to the total.
# After the loop finishes, the average is calculated by dividing the total by the total number of elements in the list.
# The average is then returned as the
# output. Both methods will give the same output, which is the average of the numbers in the list [1, 2, 3, 4, 5].
