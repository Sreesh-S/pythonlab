color=input("enter color seperated by comas:")
color_list1=color.split(',')
print(color_list1)

print("1st Color:", color_list1[0])
print("Last Color:", color_list1[-1])
color_list2 = ["Red","Orange","Black","White"]

print("color-list1 not contained in color-list2 are : ")
diff = list(set(color_list1) - set(color_list2))
print(diff)
color_int_list =[]
for color in color_list1:
    color_int_list.append(len(color))
print(f"List of integers corresponding to each color: {color_int_list}")