"""WAP TO TAKE STARTING POINT, ENDING POINT , UPDATION FROM USER AND ALSO TAKE CHOICE FOR 
PRINTING THE NUMBERS ALSO TAKE THE CHOICE FOR PRINTING THE NUMBERS IN FORWARD AND REVERSE ORDER"""
s = int(input("enter starting point "))
e = int(input("enter ending point "))
u = int(input("enter updation "))
choice = input("horizontal or vertical ")
o = input("forward or reverse order")
if(choice=="horizontal" and o=="forward"):
    for i in range(s,e,u):
        print(i,end=" ")
elif(choice=="vertical" and o=="forward"):
    for i in range(s,e,u):
        print(i)
elif(choice=="horizontal" and o=="reverse"):
    for i in range(e,s-1,-u):
        print(i,end=" ")
elif(choice=="verticle" and o=="reverse"):
    for i in range(e,s-1,-u):
        print(i)        
else:
    print("invalid input")