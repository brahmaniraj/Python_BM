"""
A function is a block of organized, reusable code that is used to perform a single, related action.
Functions provide better modularity for your application and a high degree of code reusing.
As you already know, Python gives you many built-in functions like print(), etc.
but you can also create your own functions.
These functions are called user-defined functions."""

# Defining a Function:
"""
def function_name(parameters):
    function_suite
    return [expression]

def hello(a):
    print(a)
    return

abc=hello('welcome to py world')


def sum(var1,var2):
    #creating variables inside the function
    total=var1+var2
   # print(total)
    return total


a1=sum(10,20)
print(a1)

"""

def centos(mylist):
    mylist.append([1,2,3,4,5])
    print(mylist)
    return

a1=[10,20,30,40,50]
centos(a1)