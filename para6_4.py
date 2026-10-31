try:
    try:
        print("start")
        print(error)
        print("no errors")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)