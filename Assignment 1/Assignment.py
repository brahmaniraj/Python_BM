"""
1. To calculate the length of a string.

2. To get the last part of a string before a specified character.

3. To convert a given string to all uppercase

4. To check if a string contains all letters of the alphabet.

5. To lowercase first n characters in a string

6. To split a string on the last occurrence of the delimiter.

"""

input_data = "Python assignment !! Getting started"

data_01= "PYTHON ASSIGNMENT"

print(len(input_data)) #lenght of the string

print(input_data.upper()) # convert string to uppercase

print(input_data.rsplit("!",1)[0]) #To get the last part of a string before a specified character.

str = "p.y.t.h.o.n"
print(str.rsplit('.', 1)) #To split a string on the last occurrence of the delimiter.

print(data_01[0:6].lower()+data_01[6:])



alphabets ="abcdefghijklmnopqrstuvwxyz"


import string
alphabet = set(string.ascii_lowercase)
input_string = 'The quick brown fox jumps over the lazy dog'
print(set(input_string.lower()) >= alphabet)
input_string = 'The quick brown fox jumps over the lazy cat'
print(set(input_string.lower()) >= alphabet)








