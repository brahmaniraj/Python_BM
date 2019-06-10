aTuple=('python','linux',"AWS",'azure',20,10.65,4+7j)

print(tuple(enumerate(aTuple)))

#del aTuple #deletes the entire variable
#print(aTuple)

del aTuple[1] #will throw an exception since tuple doesnt support item deletion.