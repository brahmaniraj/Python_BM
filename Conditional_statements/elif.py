#allows to check mutliple expressions for TRUE and execute a block of code as soon as one of the condition evaluates to TRUE.

"""
a = int(input("enter the value :"))

if a>100:
    print("Value of a is > than 100:" )
elif a==100:
    print("value of a is = 100 ")
else :
    print("value of a not eual to 100 or grater than 100")
"""

fee_1 = 10

if fee_1 == 20:
   print("1 - Got a true expression value")
   print(fee_1)
elif fee_1 == 15:
   print("2 - Got a true expression value")
   print(fee_1)
elif fee_1 == 10:
   print("3 - Got a true expression value")
   print(fee_1)
else:
   print("4 - Got a false expression value")
   print(fee_1)

print("Good bye!")