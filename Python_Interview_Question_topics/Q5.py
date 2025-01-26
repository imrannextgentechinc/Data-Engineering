#Qtype1 How do you find the non-matching characters in a one string?

# Give a string, find the characters that are not repeated in it

def non_matching_characters(s):
    return [char for char in s if s.count(char) == 1]

s = 'Imranali'
print(non_matching_characters(s))

# Time complexity: O(n^2) where n is the length of the string
# Space complexity: O(n) where n is the length of the string
# The count() function is used to count the occurrences of each character in the string.
# The list comprehension is used to iterate through the string and filter out the characters that are not repeated.
# Finally, the list of non-repeated characters is returned.


#Qtype2 How do you find the non-matching characters in a string?

# Given two strings, s1 and s2, find the characters that are not common in them.
# Example: s1 = 'thequickbrownfox' s2 = 'queen'
# Output: ['t', 'h', 'i', 'c', 'k', 'b', 'r', 'w', 'f', 'o', 'x']

def non_matching_characters(s1, s2):
    return list(set(s1).symmetric_difference(set(s2)))

s1 = 'thequickbrownfox'
s2 = 'queen'
print(non_matching_characters(s1, s2))
# ['t', 'h', 'i', 'c', 'k', 'b', 'r', 'w', 'f', 'o', 'x']

# Time complexity: O(n) where n is the length of the longest string
# Space complexity: O(n) where n is the length of the longest string
# The set() function is used to convert the strings into sets of characters. 
# The symmetric_difference() function is used to find the characters that are not common in the two sets.
# Finally, the result is converted back to a list and returned.


