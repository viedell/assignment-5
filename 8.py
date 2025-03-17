a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or a == c or b == c:
        print("Isosceles Triangle")
else:
    print("Scalene Triangle")
else:
    print("Not a valid triangle")
