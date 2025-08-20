text=input("enter a string:")
words=text.split()
frequency={}

for word in words:
    frequency[word]=frequency.get(word,0)+1
print("word frequency :",frequency)