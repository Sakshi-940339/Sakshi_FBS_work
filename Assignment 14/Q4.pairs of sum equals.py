nums=list(map(int,input("enter  number :").split()))
target = int(input("enter target sum :"))
pairs=set()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+ nums[j]== target:
            pairs.add((nums[i],nums[j]))
print("pairs with sum",target,":",pairs)