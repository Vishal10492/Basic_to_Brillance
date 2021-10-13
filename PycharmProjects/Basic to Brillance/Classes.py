# Classes
class Person:
    def __init__(self, name, age, idnum):
        self.name = name
        self.age = age
        self.idnum = idnum

    def output(self):
        print('Your name is ' + self.name + 'your age is ' + self.age + 'your id is ', self.idnum)


# Create multiple of class
j = Person('John', '30', '123')
m = Person('Melvin', '22', '6453')
j.output()
m.output()
print(j.age)
print(m.name)
