words=input("enter a word(space-separated):").split()
unique_word=set(words)
for word in unique_word:
    print(word,":",words.count(word))