""" WAP TO TAKE USER CHOICE HORIZONTALLY OR VERTICALLY FOR PRINTING THE NO. FROM 1 TO 50 
WITH UPDATION OF 3 """
choice = input()
if(choice=="horizontal"):
    for i in range(1,51,3):
        print(i,end=" ")
elif(choice=="vertical"):
    for i in range(1,51,3):
        print(i)
else:
    print("invalid input")            