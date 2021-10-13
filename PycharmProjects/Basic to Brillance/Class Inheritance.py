# Class Inheritance
class Person:
    def __init__(self, name, age, idnum):
        self.name = name
        self.age = age
        self.idnum = idnum

    def output(self):
        print('Your name is', self.name, 'Your age is', self.age, 'Your id number is', self.idnum)


# More about class inheritance
class Man:
    def strong(self):
        print('Men are strong')


class Child(Person, Man):
    pass


kid = Child('Vishal', '29', '123')
kid.output()
kid.strong()
