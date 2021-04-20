"""
for / while
0       10
1       9
2       8
3       7
4       6
5       5
6       4
7       3
8       2
9       1
"""

#ASSIM
y = 10

for i in range(0,10,1):
    print(i, y)
    y -= 1

####
print("\n\n")
#####

#OU
for b,c in enumerate(range(10,0,-1)):
    print(b,c)