# This program adds or subtracts two numbers provided by the user and prints the result

# User input block
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sign = input("Enter '+' to add or '-' to subtract: ")

# Conditional block to perform addition or subtraction based on user input
if sign == '+':
    print("The sum of these numbers is", a + b)
elif sign == '-':
    print("The difference of these numbers is", a - b)
else:
    print("Invalid operator entered.")