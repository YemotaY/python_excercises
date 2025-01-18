"""
Check if the first and last numbers of a list are the same
Task: Write a code to return True if the list’s first and last numbers are the same.\
      If the numbers are different, return False.

Given: 
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

Expected output:  
numbers_x is True
numbers_y is False
"""

def calculate(a):
    if(a[0]==a[-1]):
        return True
    else:
        return False

#Example 1
a = [10, 20, 30, 40, 10]
b = [75, 65, 35, 75, 30]
print(f"Checking a :{a}, result : {calculate(a)}")
print(f"Checking b :{b}, result : {calculate(b)}")
"""
Checking a :[10, 20, 30, 40, 10], result : True
Checking b :[75, 65, 35, 75, 30], result : False
"""
