class operations:
    def __init__(self,a,b):  #abc,a,b

        self.a=a
        self.b=b

    def add(self,c): # external parameter
        return ("addition of two num is",self.a+self.b+c)

    def sub(self,c):
        return ('sub of two num is',self.a-self.b-c)


a=int(input('enter a value'))
b=int(input('enter b value'))
c=int(input('enter c value'))
obj=operations(a,b)
print(obj.add(c))
print(obj.sub(c))
