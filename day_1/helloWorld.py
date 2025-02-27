# Day 1 - 30DaysOfPython

print(2 + 3)                  # addition(+)
print(3 - 1)                  # subtraction(-)
print(2 * 3)                  # multiplication(*)
print(3 / 2)                  # division(/)
print(3 ** 2)                 # exponential(**)
print(3 % 2)                  # modulus(%)
print(3 // 2)                 # floor division operator(//)

# Checking data types
print(type(10))               # int
print(type(3.14))             # float
print(type(1 + 3j))           # complex number
print(type('Ava'))            # string
print(type([1, 2, 3]))        # list
print(type({'name': 'Ava'}))  # dictionary
print(type({9.8, 3.14, 2.7})) # set
print(type((9.8, 3.14, 2.7))) # tuple

# Write an example for different Python data types
print(type(True))             # boolean

# Find an Euclidian distance between (2, 3) and (10, 8)
import math

# Define points
x1, y1 = 2, 3
x2, y2 = 10, 8

# Calculate Eclidean distance using the formula
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Print result
print("Euclidean Distance:", distance)