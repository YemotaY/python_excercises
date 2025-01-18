"""
Merge two lists using the following condition
Given two lists of numbers, write a Python code to create a new list such that the
latest list should contain odd numbers from the first list and even numbers from the second list.

Given: 
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

Expected output:  
result list: [25, 35, 40, 60, 90]
"""

def calculate(a,b):
    res = []
    for i in range(len(a)):
        if(i%2!=0):
            res.append(a[i])
    for i in range(len(b)):
        if(i%2!=0):
            res.append(b[i])
    return res

a = [10, 20, 25, 30, 35]
b = [40, 45, 60, 75, 90]
print(f"input {a},{b} res: {calculate(a,b)}")

"""
input [10, 20, 25, 30, 35],[40, 45, 60, 75, 90] res: [20, 30, 45, 75]
"""
