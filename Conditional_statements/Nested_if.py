#syntax

#if..elif..else
"""
if expression1:
    statements

elif expressions:
     statements

else:
   statements



mac_os = 100

if mac_os < 200:
   print("Expression value is less than 200")
   if mac_os == 150:
      print("Which is 150")
   elif mac_os == 100:
      print("Which is 100")
   elif mac_os == 50:
      print ("Which is 50")
elif mac_os < 50:
   print("Expression value is less than 50")
else:
   print("Could not find true expression")

print("Good bye!")

"""

x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))

if x > y:
    if x > z:
        maximum = x
    else:
        maximum = z
else:
    if y > z:
        maximum = y
    else:
        maximum = z

print("The maximam value is: ", str(maximum))