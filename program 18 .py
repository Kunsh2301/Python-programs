"""WAP TO CREATE A MINI CALCULATOR WHICH CAN PERFORM MULTIPLICATION, DIVISION, ADDITION,
SUBSTRACTION OF 2 NO.S."""
x=float(input("enter first number "))
y=float(input("enter second number"))
print("for addition enter +")
print("for substraction enter -")
print("for multiplication enter *")
print("for division enter /")
choice = input("enter ur choice")
if(choice=="+"):
    print(x+y)
elif(choice=="-"):
    print(x-y)  
elif(choice=="*"):
    print(x*y)  
elif(choice=="/"):
    print(x/y)
else:
    print("invalid input")    