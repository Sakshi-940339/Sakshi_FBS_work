dict={'name':'sakshi','age':21,'city':'pune'}
key=input("enter the key to remove :")

if key in dict:
    del dict[key]
    print("updated dictionay:",dict)
else:
    print("key not found :")