#!usr/bin/python

"""
Python supports integers , floating and complex data
Defined as int,float,complex classes in python
"""

int_data =5 #integer

print (int_data,type(int_data),id(int_data))

float_data= 76.43 #float
print(type(float_data))

acomplex_data= 5 + 5j
print(acomplex_data)

print(isinstance(acomplex_data,complex))
print(isinstance(float_data,complex))
print(isinstance(float_data,int))
print(isinstance(float_data,float))

# Built-in Functions in Numbers Datatypes: Int(),float(),complex()

#Mathematical Functions :
'''
1. Plus
2. Minus
3. Slash
4. Asterisk
5. Percent
6. Less-than
7. Greater-than
8. Less-than-or-equal-to
9. Greather-than-or-equal-to
'''

#Built-in Methods:

#1. abs() : 0-9 -absolute value (positive distance between n and zero)

print(abs(-45))

#2. ceil() : executes the smallest interger not less than x value

import math
print(math.ceil(9.87))
print(math.ceil(-9.87))

