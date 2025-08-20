str1=input("enter a first string :")
str2=input("enter a second string :")

str1 =str1.replace(" "," ")
str2 = str2.replace(" "," ")
if sorted (str1)==sorted (str2):
    print("the string are anagram ")
else:
    print("the string are not anagram ")
    