"""
a=input("enter numner1: ")
b=input("enter numner2: ")
c= int(a)/int(b)

print("division is:" ,c)

#will throw an error -    c= int(a)/int(b)
#ZeroDivisionError: division by zero
"""

"""
a=input("enter numner1:")
b=input("enter numner2:")

try:

    c=int(a)/int(b)
except Exception as e:
    print(f'Exception occured: {e}')
    c= None

print(c)
"""

"""
a=input("enter numner1:")
b=input("enter numner2:")

try:

    c=int(a)/int(b)
except ZeroDivisionError as e:
    print(f'Division by Zero Exception: {e}')
    c= None

print(c)

"""

a=input("enter numner1:")
b=input("enter numner2:")

try:

    c=int(a)/int(b)
except ZeroDivisionError as e:
    print(f'Division by Zero Exception: {e}')
    c= None
except Exception as e:
    print('Exception type:',type(e).__name__)
    c=None
finally:
    print("excecuting finally clause")
print("division is :",c)

print(c)
