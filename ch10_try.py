def devide_test(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as err:
        print(err)
        print("error : b=0")
    except:
        print("error : a is string")

devide_test(10,0)
#division by zero
#error : b=0

devide_test("a",1)
#error : a is string