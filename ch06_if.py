is_male=True
is_tall=True
is_good=True

#or and not
#if elif else
if is_male or is_tall:
    print("You are male or tall")
elif not(is_good):
    print("you are good")
else:
    print("you are female or short")
#You are male or tall

#= != > >= < <= 
def compare(a,b):
    if a>b:
        return "more"
    else:
        return "equal or less"

print(compare(5,4))
#more