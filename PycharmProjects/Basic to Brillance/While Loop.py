# While loop, keep looping as long the condition is True

'''
i = 1
while i <= 6:
    print(i)
    i += 1

# Using Flag to stop loop
i = ''
name = 'Enter your name: '
while i != 'q':
    i = input(name)
'''


# Using break and continue with while loop
i = 1
user = ''
while i <= 2:
    user = input('Insert any name: \n')
    print('You inserted ' + user)
    if user == 'Vishal':
        break
    elif user == 'Vikas':
        continue
    i += 1
