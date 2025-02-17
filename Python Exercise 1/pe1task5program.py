# Program to count the number of even and odd numbers in a series of numbers

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return even_count, odd_count

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count, odd_count = count_even_odd(numbers)
print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")