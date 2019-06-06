"""
A tuple is an immutable sequence of values of any type

tuple()

element starts with zero'th index.

"""

aTuple=('python','linux',"AWS",'azure',20,10.65,4+7j)

tuple1='python','linux',"AWS",'azure',20,10.65,4+7j

print(tuple1)

print(type(aTuple),id(aTuple),len(aTuple),tuple(enumerate(aTuple)))