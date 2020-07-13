
def good_morning (a):
    print("good Morning.....")


def patch_function(a, b=None , c=None):
    print("I patched you ")
    print("This not morning ")


good_morning = patch_function

good_morning(1)
a =1 
a = 2 
print(globals())