#find all mp3 files in my pc/latopn
"""
import os
import fnmatch

path="/Users/Administrator/Python_BM/Loops"
pattern="*.mp3"

for root,dirs,files in os.walk(path):
    for filename in fnmatch.filter(files,pattern):
        print(os.path.join(root,filename))
 """


import os
import fnmatch
#pattern = 'fnmatch_*.py'
pattern = 'fnmatch_.py'

print ('Pattern :', pattern)
print ("")

files = os.listdir('.')

for name in files:
    print ('Filename: %-25s %s' % (name, fnmatch.fnmatch(name, pattern)))