nums=list(map(int,input("enter no").split()))
nums=list(set(nums))

max_product=float('_inf')
pair=()

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        product = nums[i] * nums[j]
        if product > max_product:
            max_product = product
            pair = (nums[i] , nums[j])
print("Two no with max product:",pair,"product",max_product)
