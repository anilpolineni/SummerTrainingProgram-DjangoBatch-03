# non parameterized constructor

class student:
    def __init__(self):
        print('This is non Parameterized')

    '''def show(self,name):
              return ('welcome',name)'''


obj=student()
print(obj)
#print(obj.show('john'))


'''# parameterized constructor


class student:
    def __init__(self,name):
        print('This is parameterized constructor ')
        self.myname=name

    def show(self):
        return ('my name is',self.myname)
obj=student('john')
print(obj.show())'''

