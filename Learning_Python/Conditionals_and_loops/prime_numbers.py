import math


num = 7

for i in range(2, num):
    if num % i == 0:
        print(f"{i} is not a prime number")
        break
else:
    print(f"{i} is a prime number")






num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print(f"{i} is not a prime number")
        break
else:
    print(f"{i} is a prime number")
        


# #example 2
# #using math module

num = int(input("Enter a number: "))
sqrt_num = math.isqrt(num)
for i in range(2, sqrt_num + 1):
    if num % i == 0:
        print(f"{i} is not a prime number")
        break
else:
    print(f"{i} is a prime number")


#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
#In other words, a prime number is a number that cannot be formed by multiplying two smaller natural numbers.
#For example, the number 5 is prime because the only way to create it is by multiplying 1 and 5.
#The first few prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, and so on.
#The number 1 is not considered a prime number because it has only one positive divisor (itself).

