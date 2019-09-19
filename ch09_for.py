def for_test(i):
    for i in range(i):
        print(i)


for_test(3)
"""
0
1
2
"""

matx=[
    [ [1,2] , [3,4] ],
    [ [5,6] , [7,8] ],
]

print(matx[0][0][1])
#2

for x in matx:
    for y in x:
        for z in y:
            print(z)
"""
1
2
3
4
5
6
7
8
"""
