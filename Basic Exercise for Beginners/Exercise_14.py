"""
Print a downward half-pyramid pattern of stars
* * * * *  
* * * *  
* * *  
* *  
*
"""

def create(len):
    res = ""
    for i in range(len,0,-1):
        for y in range(0,i):
            res += "*"
        res += "\n"
    return res
    
print(create(10))

"""
**********
*********
********
*******
******
*****
****
***
**
*
"""