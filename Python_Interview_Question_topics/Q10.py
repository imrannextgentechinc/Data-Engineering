#How do you find the maximum element in an array?

#using built-in max() function
def max_element(arr):
    return max(arr)

arr = [1,2,3,4,5,6,7,8,9,10]
print(max_element(arr))

#explaination: The max() function returns the largest item in an iterable or the largest of two or more arguments.



#method 2


def max_element(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [1,2,3,4,5,6,7,8,9,10]
print(max_element(arr))


#Time Complexity: O(n)
#Space Complexity: O(1)

#Note: We can also use the built-in max() function to find the maximum element in an array.
# max_element = max(arr)
# print(max_element)
#Output : 10
