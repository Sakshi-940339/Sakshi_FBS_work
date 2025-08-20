str=input("enter a string :")
words = str.split()
num_words=len(words)
count_char =0
for ch in str:
    if ch !=" ":
        count_char += 1
print("number of words ",num_words)
print("number of charecter :",count_char)