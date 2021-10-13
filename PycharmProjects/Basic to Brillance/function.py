# Functions
def names(fname, lname):
    print('Your First name is ' + fname)
    print('Your Last name is ' + lname, '\n')


names('Vishal', 'Singh')

'''
def add(a, b):
    print(int(a) + int(b))
add(input(), input())
'''

# Multiple function call
names('Mani', 'kanta')
names(lname='Johnny', fname='Depp')


def add(a, b):
    total = a + b
    return total


print(add(4, 5))
