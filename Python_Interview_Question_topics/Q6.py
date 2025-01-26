#How do you find out if the two given strings are anagrams?

# Give two strings, s1 and s2, write a function to determine if they are anagrams of each other.
# Anagrams are words or phrases that contain the same characters in a different order.
# Example: s1 = 'listen' s2 = 'silent'
# Output: True

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = 'listen'
s2 = 'silent'
print(are_anagrams(s1, s2))

#explaining the code
#The function are_anagrams takes two strings s1 and s2 as input.
#It uses the sorted() function to sort the characters in each string.
#It then compares the sorted strings for equality using the == operator.
#If the sorted strings are equal, it returns True, indicating that the strings are anagrams.
#Otherwise, it returns False.


# Time complexity: O(n log n) where n is the length of the strings
# Space complexity: O(n) where n is the length of the strings
# The sorted() function is used to sort the characters in each string.


def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = 'one'
s2 = 'onetwo'
print(are_anagrams(s1,s2))


