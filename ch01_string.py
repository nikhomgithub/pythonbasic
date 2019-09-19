#+ \n   " \" "
name="Nikhom"

age=40
good_man=True

print('My name is '+name+ '.'+'\nI am a good man')
#My name is Nikhom.
#I am a good man

print(good_man)
#True
print(age)
#40

#lower() upper() isupper() islower()
#len()
print(name.lower())
#nikhom

print(name.upper().isupper())
#True

print(len(name))
#6
print(name[1])
#i

target="xyz"
prefix="OK"

#for
for i in prefix:
    for j in target:
        print(i+" and "+j)
"""
O and x
O and y
O and z
K and x
K and y
K and z
"""

name2="nikhom goodman"
print(name2.replace("goodman","badman"))
#nikhom badman