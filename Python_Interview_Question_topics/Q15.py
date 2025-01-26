#How do you check if an integer is even or odd?

#method 1 using user input and modulo operator

def check_even_odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
    
num = int(input("Enter the integer number: "))
print(check_even_odd(num))


#explaination:
#1. take the input from the user
#2. check if the number is divisible by 2 or not
#3. if the number is divisible by 2 then it is even otherwise it is odd



#method 2 using modulo operator and predefined number

def check_even_odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(check_even_odd(5))
print(check_even_odd(6))



#method  using bitwise operator and predefined number

def check_even_odd(num):
    if num & 1 == 0:
        return "Even"
    else:
        return "Odd"
    
print(check_even_odd(5))
print(check_even_odd(6))

#explaination:
#1. take the input from the user
#2. check if the number is divisible by 2 or not
#3. if the number is divisible by 2 then it is even otherwise it is odd
#4. using bitwise operator to check the last bit of the number


