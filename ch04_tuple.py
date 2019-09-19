#tuple can not be change after create

co=(4,5,6,7,8)

print(co)
#(4, 5, 6, 7, 8)
print(co[-1])
#8
#co[-1]=10
#TypeError: 'tuple' object does not support item assignment