#Write a program to check whether a given number is a palindrome.
#A palindrome is a number that remains the same when its digits are reversed. For example, 121 is a palindrome, as its reverse is 121. However, 123 is not a palindrome, as its reverse is 321. The program should return True if the number is a palindrome, and False if it is not. The program should take the number as input from the user.

def palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False
    
num = int(input("Enter a number: "))
if palindrome(num):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
