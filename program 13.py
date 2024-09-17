#WAP TO COUNT NO. OF EVEN AND ODD FROM 1 TO 20.
cv,co=0,0
for i in range(1,21,1):
    if(i%2==0):
        cv+=1
    else:
        co+=1
print(cv)
print(co)            