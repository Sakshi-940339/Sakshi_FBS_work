#      A          
#     A B C 
#    A B C D E        
#   A B C D E F G     
#  A B C D E F G H I  

n=5
for i in range(5):
    print(" "*(5-i-1),end=" ")
    for j in range(2*i+1):
        print(chr(65+j),end=" ")
    print()