#How do you implement binary search to find an element in a sorted array?

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    
    return -1  # Target not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

#Explanation:
#Initialization: We initialize low to the first index (0) and high to the last index (len(arr) - 1).
#While Loop: As long as low <= high, we keep checking the middle element. If it matches the target, we return the index.
#Update Search Range: If the target is smaller than the middle element, we update high to search the left half. If the target is larger, we update low to search the right half.
#Return: If the loop ends without finding the target, return -1, indicating that the element is not in the array.