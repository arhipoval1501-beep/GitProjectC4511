try:
    print("start")
    print(10/0)
    print("no errors")
except NameError:
    print("We have an error")
except ZeroDivisionError:
    print("ZeroDivisionError")

print("code after capsule")