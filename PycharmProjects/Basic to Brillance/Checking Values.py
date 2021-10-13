# Checking Values
'''
name = input('Enter your name: ')
NameList = ['Vishal', 'Vikas', 'Akash']

if name in NameList:
    print('Name is in the list')
else:
    print('Name is not in the list')

if name not in NameList:
    print('Name is not in the list')
else:
    print('Name is in the list')
'''

# if elif else statement
print('Loan Application')
salary = int(input('Enter your salary:'))

if salary >= 10000 and salary < 50000:
    print('your are eligible for Rs.5000')
elif salary >= 50000:
    print('your are eligible for Rs.', int(salary/2))
else:
    print('you are not eligible')


