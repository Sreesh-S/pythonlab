num=int(input("enter the number:"))
list=[i for i in range(1, num+1)if num % i == 0]
print("factors of number=",list)

print("\n Enter length and breadth of a rectangle:")
l=int(input("length:"))
b=int(input("breadth:"))
c = lambda x,y: x*y

print("area of rectangle :" , c(l,b))
print("\nenter side of a square:")
s=int(input("sides of a square:"))
c=lambda x: x*x
print("area of square",  c(s))