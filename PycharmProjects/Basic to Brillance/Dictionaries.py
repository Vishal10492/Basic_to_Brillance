dic = {'toyota': 'Camry', 'Cylinder': 'v6'}
print(dic['toyota'])
print(type(dic))

dic['color'] = 'White'
print(dic)

NewDic = {}
NewDic['Name'] = 'Vishal'
NewDic['Age'] = 29
NewDic['City'] = 'Nagpur'
print(NewDic)

NewDic['City'] = 'Bangalore'  # change value of key
print(NewDic)

del(NewDic['City'])  # delete key
print(NewDic)

