"""WAP TO FIND SUM OF EVEN NO.S AND ODD NO.S FROM 1 TO 50 """
e,o=0,0
for i in range(1,51,1):
    if(i%2==0):
        e+=i
    else:
        o+=i
print("sum of even" , e)   
print("sum of odd" , o)         