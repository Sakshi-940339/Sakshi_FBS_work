no=[10,12,15,20,24,30,40]
m=4
n=5

divisible=[x for x in no if x % m == 0 and x % n==0]
print("original list :",no)
print(f"no divisible by {m} and {n}",divisible)