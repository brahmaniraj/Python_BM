#count()- counts the number of occurences
"""
data=['python',"devops",'azure',10,20,40.5,3+4j]

print(data.count('DEVOPS'))

#append()

aws=[10,20,30]

aws.append(40)
print(aws)

aws.append("python")

print(aws)

aws.append(['movie','year'])

print(aws)

#del()

del aws[5]
print(aws)
#print(list(enumerate(aws)))

"""

"""
# extend()

vcs_github = ['movie','year','cast']

raw_data=[10,20,30,40]
vcs_github.extend(raw_data)

print(vcs_github)
"""
"""
#insert()

data_01=["ironman","captain america","Ironman",2001,2019]

data_02=[45,32,65,12,56,34,23]

print(list(enumerate(data_01)))

#data_01.insert(2,"Django")

data_01.insert("test")

print(data_01)

"""

"""
#remove()


data_01=["ironman","captain america","Ironman",2001,2019]

data_02=[45,32,65,12,56,34,23]

print(data_01,list(enumerate(data_01)))

data_01.remove(2001)

print(data_01,list(enumerate(data_01)))

data_01.remove("ironman")

print(data_01,list(enumerate(data_01)))

#data_01.remove("azure") #will throw exception since it is not part of the declared list.

#print(data_01,list(enumerate(data_01)))

"""

"""
#pop() - removes the last element in the list
data_01=["ironman","captain america","Ironman",2001,2019]

data_02=[45,32,65,12,56,34,23]

print(data_01,list(enumerate(data_01)))

#data_01.pop()

#print(data_01,list(enumerate(data_01)))

data_01.pop(2)

#print(data_01,list(enumerate(data_01)))

"""

"""
#reverse()

data_01=["ironman","captain america","Ironman",2001,2019]

data_02=[45,32,65,12,56,34,23]

print(data_01)

data_01.reverse()

print(data_01)

"""

"""
#sort() - Special charatersm Integers, uppercase, lower case - is the priority

data_01=["c","6","A","!","m"]

data_02=[45,32,65,12,56,34,23]

print(data_01)

data_01.sort()

print(data_01)

"""

#min(),max() - works on dedicated dadta types

data_01=["ironman","captain america","Ironman"]

data_02=[45,32,65,12,56,34,23]
print(max(data_02))

print(min(data_02))

print(max(data_01))