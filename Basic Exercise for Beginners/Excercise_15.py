"""
Get an int value of base raises to the power of exponent
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
case 1:
base = 2
exponent = 5
2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
case 2:
base = 5
exponent = 4
5 raises to the power of 4 is: 625 
i.e. (5 *5 * 5 *5 = 625)
"""
def calculate(base,exponent):
    return base ** exponent

base = 2
exponent = 5
print(f"1base {base}, exponent {exponent}, res {calculate(base,exponent)}")
base = 5
exponent = 4
print(f"2base {base}, exponent {exponent}, res {calculate(base,exponent)}")