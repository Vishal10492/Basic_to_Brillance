# Create List

animals = ['lion', 'tiger', 'dog', 'cat']
print(animals)
print(animals[0].title())
print(animals[-1].title())

# Combine and print an element with string
animal = ['lion', 'tiger', 'dog', 'cat', 'monkey']
msg = 'I love my '
print(msg + animal[2].upper())

# Change element from list
animal[3] = 'camel'
print(animal)

# Delete element from list
del animal[4]
print(animal)

# Sort() and reverse()
print(animal.sort())  # sorting doesn't work in print function
animal.sort()
print(animal)
animal.reverse()  # animal.sort(reverse=True)
print(animal)

# Using len()
print(len(animal))

# Using for Loop in list
'''for animal in animal:
    print('I love my '+animal)
    print('Thank you')
print('Last Msg')'''  # code changes animal value to 'list element in list'

# Using for Loop in range method
for value in range(1, 5):
    print(value)

for i in range(0, 4):
    print(animal[int(i)])
print(animal[0])

# using min max sum with numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
