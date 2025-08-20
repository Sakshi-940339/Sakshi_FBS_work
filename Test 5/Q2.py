n=int(input("enter a original number of coin :"))
coins=list(map(int,input("enter coin number:").split()))

missing_coin=0
for coin in coins:
    missing_coin ^=coin
print("the missing coin number is :",missing_coin)