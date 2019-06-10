#Updating dict
"""
dict1={'name': 'raj','age': 20, 'class': "second"}

print(dict1,type(dict1),id(dict1),len(dict1),dict(enumerate(dict1)))

dict1['age']=5

print(dict1)

dict1['school']='vps'

print(dict1)

print(dict1['name'])

#del dict1 -deletes entire variable

del dict1['name']

dict1.clear() #remove all the entries/elements in the dict1 variable.
print(dict1)

"""

"""
# get(),keys(),items(),values()

dict1={'name': 'raj','age': 20, 'class': "second"}

print(dict1.get('name'))
print(dict1.get('raj')) # gives none- should call only keys not the values.
print(dict1.get('name','raj')) #treats first one as key and second as value and prints just the value.

print(dict1.keys()) #prints jsut the keys dict_keys(['name', 'age', 'class'])
print(dict1.values()) #prints the values. dict_values(['raj', 20, 'second'])

print(dict1.items()) #prints output in list format, and keys are printed in tuple format. dict_items([('name', 'raj'), ('age', 20), ('class', 'second')])

"""
"""
#copy
dict1={'name': 'raj','age': 20, 'class': "second"}

print(dict1)
newdict = dict1.copy() #copies the entries from dict1 to newdict

print(newdict)


#fromkeys()
account=('name','address','accno')

a=dict.fromkeys(account) #getting keys from the account variable

b=dict.fromkeys(account,10)

#print(a) #outpu -{'name': None, 'address': None, 'accno': None}

print(b) # output-{'name': 10, 'address': 10, 'accno': 10}

"""

dict1 = {'Name': 'minnu', 'Age': 7, 'Class': 'First'}

print(dict1.setdefault('Age',None))
print(dict1.setdefault('Course','Python'))

dict2 = {'Data':'Raw','id':10}

dict1.update(dict2)

print(dict1)