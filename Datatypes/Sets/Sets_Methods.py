#union ()

a=[1,2,3,4,5]
b=[5,6,7]

print(set(a),set(b)) #output -{1, 2, 3, 4, 5} {5, 6, 7}
print(set(a).union(set(b))) #output -{1, 2, 3, 4, 5, 6, 7}

#intersection() - Returns the intersection of set a and set of elements in iterable

print(set(a).intersection(set(b))) #output -{5}

#when no common value/intersection values prints empty set.

#difference() -Difference value from the sets will be printed in the output.

print(set(a).difference(set(b))) #output-{1, 2, 3, 4}

print(set(b).difference((set(a)))) #output-{6, 7}

#update()

s=set([1,2,3,4,5])
s.update(set([5,6,7]))
print(s) #output-{1, 2, 3, 4, 5, 6, 7}  will not repeat the repeated value

#add()

s1=set([1,2,3,4,5])
s1.add(6)

print('add method :',s1) #output-add method : {1, 2, 3, 4, 5, 6}


#remove() and discard()

s2=set([1,2,3,4,5])
s2.remove(5)
print('remove method:',s2) #output-remove method: {1, 2, 3, 4} when no element to remove is present , it will throw and exception

s2.discard(2)

print('discard :',s2)
s2.discard(2)
print('discard non-existent value',s2) #it will not throw exception even though value is not present.

#pop()

s3=set([1,2,3,4,5])
print(s3.pop()) #pops out the first element. - output- 1

print(s3) #output-{2, 3, 4, 5}

#issubset() and #issuperset

s4=set([1,2,3,4,5])
s5=set([1,2])
print(s4.issubset(s5))#output- False
print(s5.issubset(s4)) #output-True
print(set([2,9,7,1]).issubset(set([1,7]))) #output - false
print(s5.issubset(s5)) #output-True

print(s4.issuperset(s5)) #output- True
print(s5.issuperset(s4)) #output-False



