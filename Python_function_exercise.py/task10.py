#10.	Write a function which prints only odd digit numbers from 0 to n, where n is the parameter of the function.
def odd_digit_numbers(n):
    for i in range(n+1):
        if i % 2 != 0:
            print(i)
odd_digit_numbers(20)



#explaning the code
#1. The function odd_digit_numbers takes an integer n as an argument.
#2. It uses a for loop to iterate through all integers from 0 to n (inclusive).
#3. Inside the loop, it checks if the current number i is odd by using the modulus operator (%).
#4. If the number is odd (i.e., i % 2 != 0), it prints the number.
#5. Finally, the function is called with the argument 20, which will print all odd numbers from 0 to 20.