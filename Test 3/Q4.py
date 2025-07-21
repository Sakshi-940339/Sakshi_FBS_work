# print pattern
# 10101
# 01010
# 10101
# 01010
# 10101
x=5
for i in range(1,x+1):
    for j in range(1,6):
        if(i+j)% 2==0:
          print(1,end="")
        else:
           print(0,end="")
    print()

    