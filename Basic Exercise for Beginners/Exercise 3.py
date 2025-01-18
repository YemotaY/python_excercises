"""
Print characters present at an even index number
Task: Write a Python code to accept a string from the user and display\
      characters present at an even index number.

Given: PYnative
Expected output:  ‘P’, ‘n’, ‘t’, ‘v’
"""

def calculate(a):
    res = ""
    for i in range(0,len(a)):
        if(i%2==0):
            res += a[i]
    print(res)

#Example 1
a = "PYnative"
calculate(a)
