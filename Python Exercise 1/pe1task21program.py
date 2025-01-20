#Write a Python program to get the frequency of elements in a list.

def frequency_of_elements(list):
    dict = {}
    for element in list:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1
    return dict

list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
print(frequency_of_elements(list))
