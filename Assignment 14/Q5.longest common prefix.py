words = input("enter string (space-septateed)").split()

def longest_common_prefix(words):
    prefix =""
    if not words:
        return prefix
    for i in range(len(min(words,key=len))):
        char_set=set(word[i] for word in words)
        if len(char_set )==1:
            prefix +=char_set.pop()
        else:
            break
    return prefix
print("longest common prefix:",longest_common_prefix(words))