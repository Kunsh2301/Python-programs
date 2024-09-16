"""WAP TO FIND THE FACTORIAL OF A NO. TAKE INPUT FROM THE USER"""
x=int(input("enter a number"))
factorial=1
for i in range(x,0,-1):
    factorial*=i
print("factorial of the number is" ,factorial)    