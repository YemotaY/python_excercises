"""
Check Palindrome Number
Write a Python code to check if the given number is palindrome.
A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number.
"""

def calculate(number):
    number_reverse = int(str(number)[::-1])
    if(number<=10):
        return False
    if(number_reverse == number):
        return True
    else:
        return False

a = 1
b = 99899
print(f"a {a} is a palindrome number: {calculate(a)}")
print(f"b {b} is a palindrome number: {calculate(b)}")

"""
a 1 is a palindrome number: False
b 99899 is a palindrome number: Trues
"""
