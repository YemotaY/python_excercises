"""
Calculate income tax
Calculate income tax for the given income by adhering to the rules below
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
"""
#Born to be a dragon slayer, forced to be a tax payer :D
def calculate(a):
    taxes = 0
    if(a>10000):
        a = a-10000 #taxfree
        taxes = 10000*0.00
    else:
        return 0
    if(a>10000):
        a =a-10000 #10%
        taxes += 10000*0.1
    else:
        return taxes
    taxes += a*0.2 #20%

    return taxes
        
income = 45000
print(f"income {income} taxes to pay: {calculate(income)}")
"""
income 45000 taxes to pay: 6000.0
"""
