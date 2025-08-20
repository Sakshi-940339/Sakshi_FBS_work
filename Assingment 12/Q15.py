str1=input("enetr a first:")
str2=input("enter a second string:")

len1=len2=0
for _ in str1:
    len1 +=1
for _ in str2:
    len2 +=1
if len1 > len2:
    print("larger string ",str1)
elif len2> len1:
    print("larger string is ",str2)
else:
    print("both string are equal in length :")


