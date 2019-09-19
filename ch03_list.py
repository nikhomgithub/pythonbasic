#list
friends=["Mee","Moo","Ma"]
#index     0     1     2
#index    -3    -2    -1
print(friends)
print(friends[:])
#['Mee', 'Moo', 'Ma']
print(friends[-3])
#Mee
print(friends[:2])
#['Mee', 'Moo']
print(friends[0:-1])
#['Mee', 'Moo']

friends2=["Jik","Joe","Jan"]
friends2.append("Jil")
friends2.insert(1,"Jab")
friends2.remove("Jan")
age=[12,13,14]
friends2.extend(age)
print(friends2)
#['Jik', 'Jab', 'Joe', 'Jil', 12, 13, 14]

friends3=["a","b","b","c"]
friends3.pop()
print(friends3)
#['a', 'b','b']
print(friends3.index("a"))
#0
print(friends3.count("b"))
#2

numbs=[1,4,6,2,3]
numbs.sort()
#[1, 2, 3, 4, 6]
print(numbs)
numbs.reverse()
print(numbs)
#[6, 4, 3, 2, 1]
n2=numbs.copy()
print(n2)
#[6, 4, 3, 2, 1]


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