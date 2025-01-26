#How do you calculate the number of vowels and consonants in a string?


# Python code to count number of vowels and consonants in a string
def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for i in s:
        if i.isalpha():
            if i in 'aeiouAEIOU':
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

s = 'Python is Awesome'
vowels, consonants = count_vowels_consonants(s)
print('Vowels:', vowels)
print('Consonants:', consonants)



#explaining the code
#1. Define a function count_vowels_consonants that takes a string as input.
#2. Initialize two variables vowels and consonants to 0.
#3. Iterate through each character in the input string.
#4. Check if the character is an alphabet using isalpha() method.
#5. If the character is an alphabet, check if it is a vowel (i.e., present in 'aeiouAEIOU').
#6. If it is a vowel, increment the count of vowels by 1.
#7. If it is not a vowel, increment the count of consonants by 1.
#8. Return the counts of vowels and consonants.
#9. Call the function with a sample string 'Python is Awesome'.
#10. Print the counts of vowels and consonants.



#method 2
def count_vowels_consonants(s):
    vowels = len([i for i in s if i in 'aeiouAEIOU'])
    consonants = len([i for i in s if i.isalpha() and i not in 'aeiouAEIOU'])
    return vowels, consonants

s = 'Python is Awesome'
vowels, consonants = count_vowels_consonants(s)
print('Vowels:', vowels)
print('Consonants:', consonants)

