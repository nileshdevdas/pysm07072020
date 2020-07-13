
list = [100, 200, 499, 283, 288, 287, 312, 22, 35, 67]

def print_numbers(numbers, filter):
    print("Numbers ********************")
    for n in numbers:
        if(filter(n)):
            print(n)

def print_numbers(numbers, filter):
    print("Numbers ********************")
    for n in numbers:
        if(filter(n)):
            print(n)

def less_than_100(num):
    return num < 100

def more_than_100(num):
    return num > 100

print_numbers(list, more_than_100)