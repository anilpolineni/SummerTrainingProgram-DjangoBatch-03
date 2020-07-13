class operations:
    def __init__(self,a,b):  #abc,a,b

        self.a=a
        self.b=b

    def add(self):
        return ("addition of two num is",self.a+self.b)


a=int(input('enter a value'))
b=int(input('enter b value'))
c=int(input('enter c value'))
obj=operations(a,b)
print(obj.add())
