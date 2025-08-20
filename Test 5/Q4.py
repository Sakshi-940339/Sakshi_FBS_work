nums=[1,3,4,1,2,6,7]

freq={}
for num in nums:
    freq[num]=freq.get(num,0)+1
print(freq)