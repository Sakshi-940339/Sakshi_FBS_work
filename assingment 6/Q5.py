#            * 
#         * * * 
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *


x=5
for i in range(x):
    for j in range(i,x):
        print(" ",end=(" "))
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

    