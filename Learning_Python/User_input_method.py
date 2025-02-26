#learning about how to get User Input and command line

input_x = input("Enter the value of x: ") #by default input takes values as string
x = int(input_x)                          #converting string to int

input_y = input("Enter the value of y: ")
y = int(input_y)

sum = x + y
print (f"The sum of x and y is: ", sum)


#lets try taking characters input from user 

chr = input("Enter the characters: ")
print(chr)

#If we want to call only one of the character then we use below format

chr = input("Enter a character: ")[0]   #Here in this line of code we are using index[0] just to print only first letter from the given input.
print(chr)


#If we want to evaluate the expression which we are passing we use the below method 
#With this evaluate (eval) method we can also evaluate the expressions given by the user expressions such as 2+3 -1 or a+b-c etc

result = eval(input('Enter an expression: '))
print(result)


#if we want to take the input from the command line


