#Write a program to check whether a given string is a palindrome or not. 
# Palindrome words have the same spelling if you reverse the string. Eg: Dad is a palindrome because it is the same when you reverse it.

#what is def: def is a keyword that is used to define a function in python.
def is_palindrome(s):
    
#Here is_palindrome is a function that takes a string as an argument and returns True if the string is a palindrome and False if it is not a palindrome. 

    return s == s[::-1] 
#Here s[::-1] is a slicing technique that reverses the string.

s = input("Enter a string: ")
if is_palindrome(s):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

