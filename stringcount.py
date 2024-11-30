
n = input("Enter a string: ")
list_string = n
newlist = [i for i in list_string.casefold()]
print(newlist)
dict = {}.fromkeys(newlist, 0)
print(dict)

for i in newlist:
    if i in dict:
        dict[i] += 1

print(f"Original String: {n}")
print(f"Character Count: {dict}")


if len(n) >= 3:
    if n[-3:] != "ing":
        print(n + "ing")
    else:
        print(n + "ly")
else:
    print(n)

list = ["Hello", "World", "programming", "python", "Advanced DS"]
print(list)

a = 0
for i in list:
    if len(i) > a:
        a = len(i)

print(f"The length of the longest word is: {a}")

n = 5

for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')
