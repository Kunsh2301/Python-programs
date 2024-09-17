#WAP TO MULTIPLY THE EVEN NO.S AND ODD NO.S FROM 1 TO 20. 
even=odd=1
for i in range(1,21,1):
    if(i%2==0):
        even*=i
    else:
        odd*=i
print("even=" , even)  
print("odd=",odd)          