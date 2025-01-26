#How do you calculate the number of numerical digits in a string?

#Method 1
def count_digits(s):
    count = 0
    for i in s:
        if i.isdigit():
            count += 1
    return count

s = "Python3.9"
print(count_digits(s))


#explain the code
#The function count_digits takes a string s as input.
#It initializes a count variable to 0 to keep track of the number of digits in the string.
#It then iterates over each character i in the string s using a for loop.
#For each character, it checks if the character is a digit using the isdigit() method.
#If the character is a digit, it increments the count variable by 1.
#Finally, it returns the total count of digits in the string.



#Method 2
def count_digits(s):
    return sum(c.isdigit() for c in s)

s = "Python3.9"
print(count_digits(s))

#Method 3
def count_digits(s):
    return len([c for c in s if c.isdigit()])
s = "Python3.9"
print(count_digits(s))

