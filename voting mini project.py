"""make a mini project for voting system to check the eligibility for vote if eligible then
take vote and print it using infinite loop."""
bjp,congress=0,0
while(True):
    print("for vote press 5\n total result then press 6\n end voting press 7")
    select=int(input())
    if( select==5):
        a=int(input("enter your age-"))
        if(a==18 or a>18):
            print("you are eligible to vote")
            print("press 1 for bjp \n press 2 for congress")
            vote=int(input())
            if(vote==1):
                print("thanku for voting you choosed bjp")
                bjp+=1
            elif(vote==2):
                print("thanku for voting you choosed congress")
                congress+=1
            else:
                print("select a valid option")
        else:
            print("you are not eligible to vote")
    elif(select==6):
        print("bjp got", bjp ,"votes")  
        print("congress got", congress, "votes")  
    elif(select==7):
        print("voting has ended")
        break
    else:
        print("invalid input")    
            
                    
    