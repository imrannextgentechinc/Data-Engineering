#3.	Write a function to accept a list of numbers and print the sum of the numbers which follows the below condition:
#a.	Using sum function
#b.	Without using sum function


list_of_numbers = input("Enter a list of numbers separated by space: ").split()


print("Sum of numbers without using sum function:", sum(int(num) for num in list_of_numbers))

print("Sum of numbers using sum function:", sum(map(int, list_of_numbers)))


#The code prompts the user to enter a list of numbers separated by spaces. It then calculates the sum of these numbers in two different ways:
#1. Without using the built-in sum function, it uses a generator expression to convert each number to an integer and sum them up.
#2. Using the built-in sum function, it uses the map function to convert each number to an integer and then sums them up.
#Finally, it prints both sums.
#The first sum is calculated using a generator expression, which is a memory-efficient way to iterate over the list.
#The second sum uses the map function, which applies the int function to each element of the list and returns an iterator.
#The sum function then takes this iterator and calculates the total.
#Both methods yield the same result, but they demonstrate different approaches to summing a list of numbers in Python.
#The code is efficient and works well for a reasonable size of input list.