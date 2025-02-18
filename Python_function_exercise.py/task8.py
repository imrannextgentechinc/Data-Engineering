
#8.	Write a function to return a 2 dimensional list which follows the rule: a[i, j] = i + j

def generate_2d_list(n):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i + j)
        result.append(row)
    return result

n = int(input("Enter the size of the 2D list: "))
two_d_list = generate_2d_list(n)
for row in two_d_list:
    print(row)

#explanation: 
# The function `generate_2d_list` takes an integer `n` as input and generates a 2D list of size `n x n`, 
# where each element at position `(i, j)` is the sum of its row index `i` and column index `j`. 
# The outer loop iterates over the rows, while the inner loop iterates over the columns, appending the sum to the current row. 
# Finally, the function returns the complete 2D list.







#Other examples

#	Write a function to return the sum of all even numbers in a given list.
def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6]
result = sum_of_even_numbers(numbers)
print("Sum of even numbers:", result)


#   Write a function to return the sum of all odd numbers in a given list.
def sum_of_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 != 0)
numbers = [1, 2, 3, 4, 5, 6]
result = sum_of_odd_numbers(numbers)
print("Sum of odd numbers:", result)


#	Write a function to return the sum of all numbers in a given list.
def sum_of_numbers(numbers):
    return sum(numbers)
numbers = [1, 2, 3, 4, 5, 6]
result = sum_of_numbers(numbers)
print("Sum of all numbers:", result)


#	Write a function to return the largest number in a given list.
def largest_number(numbers):
    return max(numbers)
numbers = [1, 2, 3, 4, 5, 6]
result = largest_number(numbers)
print("Largest number:", result)


#	Write a function to return the smallest number in a given list.
def smallest_number(numbers):
    return min(numbers)
numbers = [1, 2, 3, 4, 5, 6]
result = smallest_number(numbers)
print("Smallest number:", result)
