#How do you total all of the matching integer elements in an array?

# Given an array of integers and a target value, 
# write a function to return the total number of elements in the array that match the target value.
# Example: arr = [1, 2, 3, 4, 5, 1, 2, 1] target = 1


#method 1

array = [1, 2, 3, 1, 4, 5, 1, 2, 1]
target = int(input ("Enter the target value: "))
total = sum(1 for i in array if i == target)
print(total)

#explaining the code
#1. Define an array of integers and a target value.
#2. Use the sum() function to count the number of elements in the array that match the target value.
#3. Use a generator expression to iterate through the array and count the elements that are equal to the target value.
#4. Print the total count of matching elements.
#5. Call the function with a sample array and target value.
#6. Print the total count of matching elements.



#method 2
array = [1, 2, 3, 1, 4, 5, 1, 2, 1]
target =  int(input ("Enter the target value: "))
total = 0
for i in array:
    if i == target:
        total += 1
print(total)


#removing input and adding target value

array = [1, 2, 3, 1, 4, 5, 1, 2, 1]
target = 1
total = 0
for i in array:
    if i == target:
        total += 1
print(total)



