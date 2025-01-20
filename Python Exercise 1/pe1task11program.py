#Write a Python program to construct the following pattern, using a nested loop number.

# Number of rows for the pattern
n = 9

# Outer loop for each row
for i in range(1, n + 1):
    # Inner loop to print the number i, i times in each row
    for j in range(i):
        print(i, end="")  # Print the number i
    print()  # Move to the next line after each row


#Here we can also do this are using The range(1, 10) then loop goes from 1 to 9. 
# The print(str(i) * i) prints the string representation of i, i times.

#for i in range(1, 10):
   # print(str(i) * i)