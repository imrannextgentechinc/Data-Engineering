#Write a  Python program to find the second smallest number in a list.

def second_smallest(numbers):
    # Remove duplicates by converting the list to a set
    unique_numbers = set(numbers)

    # If there are fewer than 2 unique numbers, return None
    if len(unique_numbers) < 2:
        return None

    # Sort the unique numbers and return the second smallest
    sorted_numbers = sorted(unique_numbers)
    return sorted_numbers[1]

# Example usage
numbers = [5, 1, 9, 2, 3, 7, 1]
result = second_smallest(numbers)

if result is not None:
    print(f"The second smallest number is: {result}")
else:
    print("There is no second smallest number.")
