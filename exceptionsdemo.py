# try:
#     ##a / b
#     open('d:/abc.xxx')
#     print("next line")
# except ZeroDivisionError as e:
#     print("Ooops Exception Occured")
#     print(e)
# except Exception as e1:
#     print("In Generic Exception")
#     print(e1)
# finally:
#     # a finally block will get executed whether there is a way or not
#     print("Whether a exception or not i will still execute ")

# How can i raise a exception


a = 19
b = 1


def add(a, b):
    if a <= 0:
        raise Exception('No You cannot have such value')
    else:
        print(a+b)

try:
    add(0, 10)
except Exception as e2:
    print(e2)


# try:
#     a/b
#     print("xxxxxx")
# except Exception as e:
#     print("In Exception")
# finally:
#     print("Anyways ")
