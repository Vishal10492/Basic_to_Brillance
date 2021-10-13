# First Simple Program

name = input('What is your name?\n')
age = input('What is your age?\n')
print('Thank You for using my program')
print('Hi', name, 'Your age is', age)

# Simple program to calc age

print('Answer the question to know your age')
name = input('Name:')
print('What is your age?', name, '?')
age = int(input('age: '))
days = age*365
minutes = age*365*24*60
seconds = minutes*60
print(name, 'has been alive for', days, 'days', minutes, 'minutes', seconds, 'seconds')
print('Thanks')
