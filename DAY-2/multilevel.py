class classA:
    a=10
    b=20
    def display1():
        return "i''m from display1"

class classB(classA):
    c=30
    d=40
    def display2():
        return "i'm from display2"


class classC(classB):
    e=50
    f=60

    def display3():
        return "i'm from display3"

obj=classB
print(obj.a)
print(obj.display1())



