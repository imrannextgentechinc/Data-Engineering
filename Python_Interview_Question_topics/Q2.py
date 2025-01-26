#How do you determine if a string is a palindrome?

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('radar'))
print(is_palindrome('hello'))

#explain the code
#The [::-1] slicing syntax is used to reverse the string.
#The reversed string is then compared to the original string using the equality operator ==.
#If the two strings are equal, the function returns True, indicating that the string is a palindrome.
#Otherwise, it returns False.
