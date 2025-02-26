# Example program using break, continue, and pass

# Using break
print("Using break:")
for i in range(10):
    if i == 5:
        break
    print(i)

# Using continue
print("\nUsing continue:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Using pass
print("\nUsing pass:")
for i in range(10):
    if i % 2 == 0:
        pass  # Placeholder for future code
    else:
        print(i)



#print first 50 fibonacci numbers
print("\nFibonacci numbers:")
a, b = 0, 1
for i in range(50):
    print(a, end=", ")
    a, b = b, a + b
    if i == 49:
        print("\n")
# Using break to exit the loop
print("Using break to exit the loop:")
for i in range(50):
    if i == 10:
        break
    print(i, end=", ")
print("\n")
# Using continue to skip even numbers
print("Using continue to skip even numbers:")
for i in range(50):
    if i % 2 == 0:
        continue
    print(i, end=", ")
print("\n")
# Using pass as a placeholder
print("Using pass as a placeholder:")
for i in range(50):
    if i % 2 == 0:
        pass
    else:
        print(i, end=", ")
print("\n")






#check a given number is prime or not
print("Using break to check if a number is prime:")
number = 29
is_prime = True
for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
print("\nUsing continue to skip even numbers:")
number = 29
is_prime = True
for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        is_prime = False
        continue
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
print("\nUsing pass as a placeholder:")
number = 29
is_prime = True
for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        is_prime = False
        pass
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
print("\n")
# Using break to exit the loop
print("Using break to exit the loop:")
for i in range(50):
    if i == 10:
        break
    print(i, end=", ")
print("\n")
