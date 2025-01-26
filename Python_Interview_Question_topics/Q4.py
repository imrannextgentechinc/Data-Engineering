#How do you find the count for the occurrence of a particular character in a string?

def count_char(string, char):
    count = 0
    for i in string:
        if i == char:
            count += 1
    return count

string = "Python is a programming language"
char = "a"
print(count_char(string, char))

#explain the code
#The function count_char takes two arguments: a string s and a character char.
#It initializes a count variable to 0 to keep track of the number of occurrences of the character in the string.
#It then iterates over each character i in the string s using a for loop.
#For each character, it checks if the character is equal to the specified character char.
#If the character matches, it increments the count variable by 1.
#Finally, it returns the total count of occurrences of the character in the string.

#Method 2
def count_char(string, char):
    return sum(c == char for c in string)

string = "Python is a programming language"
char = "a"
print(count_char(string, char))

