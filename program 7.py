""" WAP TO TAKE STARTING POINT, ENDING POINT , UPDATION FROM USER AND ALSO TAKE CHOICE FOR 
PRINTING THE NUMBERS. """
s = int(input("enter starting point "))
e = int(input("enter ending point "))
u = int(input("enter updation "))
choice = input(" horizontal or vertical")
if(choice=="horizontal"):
    for i in range(s,e,u):
        print(i,end=" ")
elif(choice=="vertical"):
    for i in range(s,e,u):
        print(i)
else:
    print("invalid input")