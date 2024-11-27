dict1 = {2: "orange", 3: "banana", 1: "apple"}
print(f"Dictionary i: {dict1}")
I = list(dict1.items())
I = sorted(I)
print('Ascending order is:', I)

I = list(dict1.items())
I = sorted(I, reverse=True)
print('Descending order is:', I)

dict2 = {4: "plum", 5: "cherry"}

print(f"Dictionary i: {dict2}")

dict1.update(dict2)
print(f"Dictionary after merging: {dict1}")
