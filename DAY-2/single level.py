class classA:
    a=10
    b=20

    def method1():
        return "i'm from classA"


class classB(classA):
    c=30
    d=40

    def method2():
        return "i'm from classB"

obj=classB
print(obj.a)
print(obj.method1())


    
    
