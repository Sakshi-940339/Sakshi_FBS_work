list1=[5,3,7,5,2,5,9,5]
remove=5
new_list=[ x for x in list1  if x !=remove]

print("original list", list1)
print(f"after removing all accurance of {remove}:",new_list)

