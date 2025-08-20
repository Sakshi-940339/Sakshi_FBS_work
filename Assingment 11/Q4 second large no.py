num=list(map(int, input("enter a number sepratrd by space").split()))
n= len(num)
for i in range(n):
    for j in range(0, n-i -1):
        if num[j]> num[j+1]:
            num [j ],num[j+1] = num[j+1],num[j]
print("second large no ", num[-2])
