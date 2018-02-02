import random
count=0
while(count<100):
     
         
        n=input("enter 'r' to roll a dice")
        if(n=='r'):
            r=random.randint(1,6)
            count=count+r
            print("your random number is ",r)
            print("you are in position",count)
            if count>100:
                print(" ur position is greater than 100 pleae try again")
                count=count-r
            elif count==100:
                print("U Won")
                  
               
        elif count==8:
            count=37
            print("its a ladder climb up",count)
        elif count==11:
                count=2
                print("its a snake come down",count)
        elif count==13:
                count=34
                print("its a ladder climb up",count)
        elif count==25:
                count=4
                print("its a snake come down",count)
        elif count==38:
                count=9
                print("its a snake come down",count)
        elif count==40:
                count=68
                print("its a ladder climb up",count)
        elif count==52:
                count=81
                print("its a ladder climb up",count)
        elif count==65:
                count=46
                print("its a snake come down",count)
        elif count==76:
                count=97
                print("its a ladder climb up",count)
        elif count==89:
                count=70
                print("its a snake come down",count)
        elif count==93:
            count=64
            print("its a snake come down",count)
        elif count==100:
            print("U Won",count)

                
       

 

                  
           


       
     
        
     
                
        
       


      
                
