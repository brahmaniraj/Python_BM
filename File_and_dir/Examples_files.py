"""file=open("test.txt")
#print(file.read())
#file.close()

print(file.tell())
print(file.read())

print(file.tell())
print(file.seek(0))
print(f"reading a line : {file.readline()}")
print(f"remaining lines: {file.readlines()}")

file.close()

"""

"""file=open("test.txt",'a')

file.write("Adding lines to the text files")

file.close()

"""

import os
try:
    file=open("test.txt","r")
    char={}

    for line in file.readlines():
        for c in line.strip():
            char[c]=char.get(c,0) + 1

    for item in char.items():
        print(item)
finally:
    file.close()


