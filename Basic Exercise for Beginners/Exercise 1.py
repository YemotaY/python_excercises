"""
Calculate the multiplication and sum of two numbers
Task: Given two integer numbers, write a Python code to return their product only if the product is equal to\
      or lower than 1000. Otherwise, return their sum.

Given: number1 = 20, number2 = 30
Expected output: The result is 600
"""

def calculate(a,b):
    if(a*b<=1000):
        return a*b
    else:
        return a+b

#Example 1
a = 20
b = 30
print("1The result is "+ str(calculate(a,b)))
#1The result is 600

#Example 2
a = 40
b = 30
print("2The result is "+ str(calculate(a,b)))
#2The result is 70