import sys

#file=open("/Users/Administrator/abc.txt")
"""
for i in file:
    try:
        file=open(i,'r')
    except IOError as e:
        print("cannot open",e)
    else:
        print(i,"has",len(file.readline()),'lines')
        file.close()

"""
import os

#print(os.getcwd()) #get current working directory

#print(os.listdir("C:/Users/Administrator/Python_BM/ExceptionHandling")) #list of files in the directory

#print(os.uname())

#print(os.getpid())

os.mkdir("test")