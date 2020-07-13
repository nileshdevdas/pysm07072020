
# def callback(a, b):
#     print("doing it lately")
#     print("Something more....")


# def action(p1):
#     # p1 is callable // its a function body callabled
#     # why shuold i pass a function to a function Things much much easies and much much
#     # extensible
#     # SET OF ACTIVITIES WHIT WHAT VALUES YOU WANT TO DO

#     p1(10,12)


# action(p1=callback)

# def filter_criteria(obj):
#     return obj > 100

#  list.filter(filter_criteria)

#  # a function can return a function
#  # a function can accept function as parameter

# # how does this work
# # a function that accepts a function


def hello_world(p1):
    message = "hello world for me"
    print(p1(message))


def filter_me(message):
    msg = message.split(" ")
    return msg[0]


def filter_me1(message):
    msg = message.split(" ")
    return msg[1]


def filter_me2(message):
    msg = message.split(" ")
    return msg[2]

#hello_world(filter_me2)
######   a function can return a function ######

def my_function():
    def r_function(xx):
        print(xx)
    return r_function
 
a = my_function()
a("yyyy")

























