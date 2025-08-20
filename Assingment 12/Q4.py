str=input("enter a string :")
if(len(str)< 2):
    print("string is not to sort to swap:")
else:
    new_str=str[-1]+str[1:-1] + str[0]
print("new string ",new_str)

