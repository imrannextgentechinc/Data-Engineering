#Method for using while loops
#First is the initialization
#second is the condition
#third is the increment/decrement

#Imp when we are using while loop inside of while loop is called as nested while loop


# Prints numbers from 1 to 100 but skips numbers divisible by 3, 6, and 9


x = 1
while x <= 100:
    if x % 3 == 0 or x % 6 == 0 or x % 9 == 0:
        x += 1
        continue
    print(x)
    x += 1



a = 1

while a  <= 5:
    print('Hello Ali', end = ' ')
    b = 1
    while b <= 4:
        print("Thanks", end = ' ')
        b = b+1
    a = a+1
    print()

#Example 1 with increment
#Prints 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

#Example 2 with decrement
#Prints 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

#Example 3

#if you want to break out of a while loop
#You can use the break statement
#Example 4
#Prints 1 to 10 but breaks out of the loop when i is 5
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
#Example 5
#Prints 1 to 10 but skips 3
#You can use the continue statement
i=1
while i <= 10:
    if i == 3:
        continue
    print(i)
    i += 1



#Example 6
#Prints 1 to 10 but skips 5
i = 1
while i <= 10:
    if i == 5:
        continue
    print(i)
    i += 1


