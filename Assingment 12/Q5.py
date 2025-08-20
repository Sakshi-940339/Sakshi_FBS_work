str=input("enter a string:")
vowel="aeiouAEIOU"
count=0
for char in str:
    if char in vowel:
        count +=1
print("number of vowel in the string :",count)