
#The math module in Python provides access to various mathematical functions and constants. 
#It is part of the Python Standard Library, so you don't need to install anything extra to use it. 
#You can import the math module using the import statement.

#Here's a brief overview of some commonly used functions and constants in the math module:

#Common Functions
#math.sqrt(x): Returns the square root of x.
#math.pow(x, y): Returns x raised to the power of y.
#math.sin(x), math.cos(x), math.tan(x): Returns the sine, cosine, and tangent of x (where x is in radians).
#math.log(x, base): Returns the logarithm of x to the given base. If the base is not specified, it returns the natural logarithm (base e).
#math.factorial(x): Returns the factorial of x.

#Constants
#math.pi: The mathematical constant π (pi).
#math.e: The mathematical constant e (Euler's number).

#Example Usage
# Here's an example of how to use some of these functions and constants:

import math

# Calculate the square root of 16
sqrt_16 = math.sqrt(16)
print(f"The square root of 16 is {sqrt_16}")

# Calculate 2 raised to the power of 3
power = math.pow(2, 3)
print(f"2 raised to the power of 3 is {power}")

# Calculate the sine of pi/2 radians
sine_pi_over_2 = math.sin(math.pi / 2)
print(f"The sine of pi/2 is {sine_pi_over_2}")

# Calculate the natural logarithm of e
log_e = math.log(math.e)
print(f"The natural logarithm of e is {log_e}")

# Calculate the factorial of 5
factorial_5 = math.factorial(5)
print(f"The factorial of 5 is {factorial_5}")




# Calculate the floor of 3.7
floor_3_7 = math.floor(3.7)
print(f"The floor of 3.7 is {floor_3_7}")

# Calculate the ceiling of 3.7
ceil_3_7 = math.ceil(3.7)
print(f"The ceiling of 3.7 is {ceil_3_7}")




