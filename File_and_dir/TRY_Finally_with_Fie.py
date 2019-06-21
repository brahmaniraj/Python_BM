#TRY FINALLY
"""try:
    file=open("test.txt",'r+')
    print(file.readline())
    print(file.readlines())

finally:
    file.close()
"""

#with statement:

with open("test.txt",'r') as myfile:
    print(myfile.read())

    myfile.close()