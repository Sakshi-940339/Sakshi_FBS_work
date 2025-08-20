dict={'name':'sakshi','age':21,'city':'pune'}
key=input("enter the key to check :")
if key in dict:
    print(f"key '{key}' exist with value {dict[key]}")
else:
    print(f"key'{key}' does not exit")
    