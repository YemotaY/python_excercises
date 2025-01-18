"""
Remove first n characters from a string
Task: Write a Python code to remove characters from a string from 0 to n and return a new string.

Given: PYnative,4
Expected output:  "tive"
"""

def calculate(str,start_idx):
    if(start_idx<len(str)):
        print(str[start_idx:len(str)])

#Example 1
str = "PYnative"
start_idx = 4
calculate(str,start_idx)
