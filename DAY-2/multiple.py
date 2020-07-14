class classA:
    p,q=100,200
    def method1():
        return "i'm from method1"


class classB:
    r,s=300,500
    def method2():
        return "i'm from method2"


class classC(classA):
    u,v=10,20
    def method3():
        return "i'm from method3"


class classD(classC,classB):
    x,y=30,40
    def method4():
        return "i'm from method4"

obj=classD

print(obj.r)

print(obj.method2())

