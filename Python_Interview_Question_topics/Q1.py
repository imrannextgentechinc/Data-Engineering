#How do you reverse a string?


#Method 1
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello World"))

#explain the code
#The [::-1] slicing syntax is used to reverse the string.
#The slicing syntax [start:stop:step] is used to extract a subsequence from the original sequence.
#In this case, the start and stop indices are omitted, and the step is -1, which means that the sequence is reversed.
#Finally, the reversed string is returned.



#Method 2
def reverse_string(s):
    return ''.join(reversed(s))
print(reverse_string("Hello World"))

#Method 3
def reverse_string(s):
    return ''.join(s[i] for i in range(len(s)-1, -1, -1))
print(reverse_string("Hello World"))

