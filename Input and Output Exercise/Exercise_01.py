"""
Accept numbers from a user
Write a program to accept two numbers from the user and calculate multiplication
"""
try:
    number1 = int(input("Please enter a number\n"))
    number2 = int(input("Please enter a number\n"))
    r = number1 / 2
    r = number2 / 2
except Exception as e:
    print('Not a number in one of inputs.')

print(number1*number2)