#2.	Write a function to print the tables of a given number till 10.

import math

num = int(input("Enter a number: "))

def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

print_table(num)
