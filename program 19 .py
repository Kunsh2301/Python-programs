#WAP TO CHECK THE ELIGIBILITY FOR VOTE IF ELIGIBLE THEN VOTE AND PRINT IT.
x,y,z=0,0,0
v=int(input("enter ur age-"))
if(v>18):
    print("Press 1 for BJP")
    print("Press 2 for Congress")
    c=int(input("enter your choice"))
    if (c==1):
         x=x+1
    if(c==2):
          y=y+1
    else:
           print("invalid ")
else:
    print("u are not eligible")

print("Total Vote of BJP = ",x)
print("Total Vote of Congress = ",y)