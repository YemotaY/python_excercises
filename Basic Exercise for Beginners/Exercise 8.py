"""
Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""
res = ""
for i in range(1,6):
    if i != 1 : res += "\n"
    for y in range(i):
        res += str(i)
print(res)

"""
1
22
333
4444
55555
"""
