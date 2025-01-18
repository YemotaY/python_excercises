"""
Display numbers divisible by 5
Task: Write a Python code to display numbers from a list divisible by 5

Given: [10, 20, 33, 46, 55]

Expected output:  
Divisible by 5
10
20
55
"""

def calculate(a):
    res = []
    for i in range(0,len(a)):
        if(a[i]%5==0):
            res.append(a[i])
    return res

#Example 1
a = [10, 20, 33, 46, 55]
print(f"Checking a :{a}, result : {calculate(a)}")
"""
Checking a :[10, 20, 33, 46, 55], result : [10, 20, 55]
"""
