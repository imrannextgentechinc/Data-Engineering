#Write a Python program to get the largest number from a list. Using both loop and max function.

#List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#what is loop? 
# A loop is a sequence of instructions that is continually repeated until a certain condition is reached.

#Using loop
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
print("Largest number using loop:", max_num)

#what is max function? 
# It returns the largest item in an iterable or the largest of two or more arguments.

#Using max function
print("Largest number using max function:", max(numbers))
