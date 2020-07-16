class Outer:
    class Inner:
        class InnerInner:
            pass


print(Outer)
print(Outer.Inner)
print(Outer.Inner.InnerInner)

outer = Outer()
inner = Outer.Inner()
inner1 = Outer.Inner.InnerInner()
print(outer)
print(inner)
print(inner1)


# python lambda

def add(a, b):
    return a + b


# anonymous single line function
v = lambda a, b: a + b

print(v(1, 2))


def app(filter):
    print(filter(1,2))


app(v)
