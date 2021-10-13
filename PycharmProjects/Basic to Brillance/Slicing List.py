# Making slicing list
OS_list = ['Mac', 'Windows', 'Linux', 'Android', 'iOS']
copy_OS_list = OS_list
print(OS_list[:5])
print(OS_list[1:4])  # it will not include list number i.e. 4
print(OS_list[-3:5])

# Using for loop with slicing list
for OS_list in OS_list[0:5]:
    print(OS_list)
print(OS_list)
print(copy_OS_list)  # Copylist using slicing list
