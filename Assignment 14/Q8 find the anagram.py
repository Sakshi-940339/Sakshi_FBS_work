words= input("enter word (space-sperated):").split()
anagram ={}

for word in words:
    key ="".join(sorted(word))
    if key not in anagram:
        anagram[key]=set()
    anagram[key].add(word)
print("grouped anagram")
list(anagram.values())


