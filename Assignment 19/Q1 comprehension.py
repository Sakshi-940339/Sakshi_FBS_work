#1. all number from 1-1000 divisible by 8

num = [n for n in range(1,1001) if n % 8==0]
print(num)


#2.find the all num form 1-1000 that ave a 6 in them

num=[n for n in range(1,1000) if '6' in str(n)]
print(num)

#3 count the no of space in a string

s=input("enter a string")
space=s.count(" ")
print("number of space",space)

#4. remove all vowel a string
s=input("entera string:")
vowels="aeiouAEIOU"
result="".join([ch for ch in s if ch not in vowels])
print("string without vowel:",result)

# #5.find all words in a string thet are less then 5 laters 

s=input("enter a string:")
words=[word for word in s.split() if len(word) < 5]
print("word with less than 5letters:",words)

# #6. dictionary comprechension to count length of each word
s= input("enter a sentance:")
word_lengths={word:len(word) for word in s.split()}
print("word length:",word_lengths)

#7.nested list comprehension number from 1-1000 divisible by any single digit (2-9)
num=[n for n in range (1,1001) if any(n % d==0 for d in range(2,10))]
print(num)
