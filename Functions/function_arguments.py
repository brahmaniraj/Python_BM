"""
1. Required Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-length Arguments
"""

#Required arguments
"""
def hello(a):
    print(a)
    return

#val="Brahmani" #Creating variable
hello(10) #accesing/calling a function, call a variable or a  value
hello("Brahmani")

"""
#Keyword Arguments
"""
def hello(abc):
    print(abc)
    return

hello(abc="welcome")



def data(name,age):
    print(f"Name : {name}")
    print(f"Age : {age}")
    return

data(name="raj",age="20")

"""

# Default arguments
"""
def data(name,age=23):  #in this case age is default arguemnts
    print(f"Name : {name}")
    print(f"Age : {age}")
    return

data(name="raj",age="20") #age=20 will override the value that is defined the function.

"""

#variable-length arguments

def info(var1,*vartuple):
    #print(var1)
    for i in vartuple:
        print(i)
    return


info(10,20,30,40,50,60,70,80,90)