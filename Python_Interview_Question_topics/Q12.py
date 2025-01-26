#How do you print a Fibonacci sequence using recursion?

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))


#explanation
#The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
#The Fibonacci sequence is defined by the recurrence relation:
#Fn = Fn-1 + Fn-2
#with seed values
#F0 = 0 and F1 = 1.
#The Fibonacci sequence is named after Italian mathematician Leonardo of Pisa, known as Fibonacci.
#In this program, we are using a recursive function to find the Fibonacci sequence of a given number of terms.
#The function takes an integer n as input and returns the nth Fibonacci number.
#We then iterate over the range of n and print the Fibonacci sequence using the recursive function.


#method 2

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))

