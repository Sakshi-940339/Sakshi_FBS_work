str=input("enter a string :")
result=""
for i in range(len(str)):
    if i % 2==0:
        result += str[i]
print("string after removing odd index charecter :",result)