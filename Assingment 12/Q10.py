str1=input("enter first string :")
str2=input("enter secount string :")

len1 =len2=0
for _ in str1:
    len1 += 1
for _ in str2:
    len2 +=1
if len1 > len2:
    print("large string is :",str1)
elif len2 > len1 :
    print("large string is",str2)
else:
    print("both string are equal in length ")