"""
DocString my first python application
"""
# with no params
def hello():
    pass
# with params
def hello1(a, b, c):
    pass
# with default value
def hello_world(a, b=10):
    """
     Sample Function
    """
    print(a)
    print(b)
    print("Hello World")
# variable args to a parameter
def hello_world1(*a):
    print(a)
# with Varibale keywords
def hello_world2(**a):
    print(a["username"])
    print(a["password"])
#wwith vargs and kwargs 
def hello_world3(*args, **kwargs):
    print(args)
    print(kwargs)

def login(username , password):
    print(username)
    print(password)
## invocations 
#hello_world(1, 20)
#hello_world(b=200, a=10)
# hello_world1(1,2,3,#4,5,6,7)
#hello_world2(username=998876, password="password")
#hello_world3(1, 2, 3, 4, 5, a=10, b=20, c=330)

#login("xxx", "xxxx")
#login(username="xxxx", password="xxxxx");
#login(password="Xxxx", username="xxx")


def foo(a, b=100):
    print(a)
    print(b)


foo(b=909, a=100)
