emp={
    "Jan":13,
    "Feb":12,
    "Mar":11
}
print(emp)
{'Jan': 13, 'Feb': 12, 'Mar': 11}

print(emp["Jan"])
#13

print(emp.get("Jan"))
#13

print(emp.get("Apr",15))
#15