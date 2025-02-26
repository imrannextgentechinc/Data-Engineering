

#basic for loop in python using range function

i = 0
for i in range(10):
    print(i)

#if we use for loop inside of for loop then it is called as nested for loop
for i in range(10):
    for j in range(5):
        print(i,j)


#for loop using math module to find square root of numbers from 1 to 500
import math
from math import sqrt

def sqrt_value(i):
    return sqrt(i)
for i in range(1,500):
    sqrt_value(i) == math.sqrt(i)
    print(f"Square root value of :", (i))
    print(sqrt_value(i))






#using if statement inside for loop
for i in range(10):
    if i%2==0:
        print(i)
    else:
        print("odd",i)

#for loop using list
list1 = [1,2,3,4,5]
for i in list1:
    print(i)

#for loop using string
string1 = "hello world"
for i in string1:
    print(i)

#for loop using tuple
tuple1 = (1,2,3,4,5)
for i in tuple1:
    print(i)

#for loop using dictionary
dict1 = {"a":1,"b":2,"c":3}
for i in dict1:
    print(i)

#for loop using set
set1 = {1,2,3,4,5}
for i in set1:
    print(i)

#for loop using range function with step value
for i in range(1,10,2):
    print(i)


#for loop using range function
for i in range(10):
    print(i)

#for loop using range function with negative step value
for i in range(10,0,-1):
    print(i)

