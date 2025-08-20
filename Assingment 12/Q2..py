str=input("enter a sentence:")
n=int(input("enter a index of the charecter to remove:"))
list1=str[:n] + str[n+1:]

print("string after removel ",list1)