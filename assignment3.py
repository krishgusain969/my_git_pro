#TASK 1
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# function call
num = 5
result = factorial(num)
print("Factorial of", num, "is:", result)

#TASK 2
import math

# user input
num = float(input("Enter a number: "))

# calculations
root = math.sqrt(num)
log = math.log(num)
sine = math.sin(num)

# display results
print("Square root:",root)
print("Natural logarithm:",log)
print("Sine:", sine)
