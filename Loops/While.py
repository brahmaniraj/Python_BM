"""a_value=1

while(a_value<=10):
    print("Printing the value " ,sep ="::" )
    a_value=a_value+1

print("not in while loop anymore")
"""

passWord = ""

while passWord != "redhat":
    passWord = input("Please enter the password: ")
    if passWord == "redhat":
        print("Correct password")
    elif passWord == "admin@123":
        print("It was previously used password")
    elif passWord == "Redhat@123":
        print("This is your recent changed password")
    else:
        print("Incorrect Password- try again")