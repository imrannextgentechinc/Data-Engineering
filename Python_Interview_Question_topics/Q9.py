#How do you reverse an array?
# Given an array of integers, write a function to reverse the elements of the array.
# Example: arr = [1, 2, 3, 4, 5]

arr = [1,2,3,4,5,6,7,8,9]
arr.reverse()
print(arr)

#explaining the code
#1. Define an array of integers.
#2. Use the reverse() method to reverse the elements of the array.
#3. Print the reversed array.


#method 2
arr = [1,2,3,4,5,6,7,8,9]
arr = arr[::-1]
print(arr)

#explaining the code
#1. Define an array of integers.
#2. Use the slicing operator to reverse the elements of the array.
#3. Print the reversed array.
