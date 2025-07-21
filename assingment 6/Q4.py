# A 
# A B       
# A B C     
# A B C D   
# A B C D E 

for i in range(1,6):
    x=65
    for j in range(1,i+1):
        print(chr(x),end=" ")
        x+=1
    print()