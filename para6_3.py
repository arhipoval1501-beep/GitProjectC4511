try:
    print("start")
    print(10/0)
    print("no errors")
except (NameError, ZeroDivisionError):
    print("We have en error")


print("code after capsule")