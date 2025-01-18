"""
Get each digit from a number in the reverse order.
For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits
"""

def calculate(a):
    res = ""
    for i in range(len(str(a)),0,-1):
        res += " "+str(a)[i-1]
    return res
        
a = 7536
print(f"input {a} res: {calculate(a)}")
"""
input 7536 res:  6 3 5 7
"""
