#How do you sort an array of integers in ascending order?

# Method 1
arr = [3, 1, 2, 4, 5]
def sort_array(arr):
    arr.sort()
    return arr

print(sort_array(arr))


#explaination:
# The sort() method sorts the elements of a given list in a specific order - Ascending or Descending.
# The sort() method changes the original list and returns None.
# The sorted() function returns a sorted list of the specified iterable object.
# You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.




# Method 2
arr = [5,9,7,6,4,3,2,1,8]
def sort_array(arr):
    return sorted(arr)

print(sort_array(arr))

