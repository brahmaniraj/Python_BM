##re module- sub () method
"""
import re

#re.sub(paatern=,repl=,string=,max()flags=)

data= '2004-959-559 #this is phone number'

num=re.sub(r'#.*$',"",data)

print(f"phone number is {num}")

num1=re.sub(r'\D',"",data) #non-digists

print(num1)"""

"""import re

text='abbaaabababaabbaaabb'

pattern='ab'

for match in re.findall(pattern,text):
    print(f"Found Match {match}")"""

"""import re

pattern ='this'

text="Does this text match the pattern?"

match=re.search(pattern,text)

s=match.start()
e=match.end()

print('Foubd "%s" in "%s" from %d to %d ("%s")' % \ """


import re


# Lets use a regular expression to match a few date strings.
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24 August 9 Dec 12",re.M|re.I)
for i in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    print ("Full match: %s" % (i))
# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for i in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print ("Match month: %s" % (i))

# If we need the exact positions of each match
regex = r"([a-zA-Z]+) \d+"

matches = re.finditer(regex, "June 24, August 9, Dec 12")

for i in matches:
    # This will now print:
    #   0 7
    #   9 17
    #   19 25
    # which corresponds with the start and end of each match in the input string
    print ("Match at index: %s, %s" % (i.start(), i.end()))




