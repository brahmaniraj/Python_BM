"""
Data Structures: Sets
A set is an unordered collection without duplicates.
When printed, iterated upon, or converted into a sequence,
its elements will appear in an arbitrary, implementation-dependent order.
"""

a=set()

print(a,type(a),id(a))

abc=set(('a','b,','A','c','a'))

print(abc,type(abc))

#output - {'b,', 'a', 'A', 'c'} <class 'set'>

adict=set({1:10,2:20,3:30,2:40}) #curly braces dictionary

print(adict,type(adict))
#output -{1, 2, 3} <class 'set'>

print(set('abcdefABCDEFabcdef'))

print(set(['abcdef','ABCDEF','abcdef',1020,1020]))

print(set(('abcdef','ABCDEF','abcdef',1020,1020)))

print(set({1:10,2:20,3:30,2:40}))

a1=('abcdefABCDEFabcdef')
print(a1,type(a1)) #it is string datatype

a2=['abcdef','ABCDEF','abcdef',1020,1020]
print(a2,type(a2)) #output - List datatype

a3={1:10,2:20,3:30,2:40}
print(a3,type(a3)) #output - Dict datatype

a4=('abcdef','ABCDEF','abcdef',1020,1020)
print(a4,type(a4))  #output- tuple

