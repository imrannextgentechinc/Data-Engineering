#4.	Write a function to accept the number of rows for the pattern and print that many number of rows.

import math

n = int(input("Enter the number of rows: "))

def print_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print("\r")

print_pattern(n)
