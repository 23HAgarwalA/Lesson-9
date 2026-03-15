a = int(input("Please input a number"))
b = int(input("Please input a number"))
c = int(input("Please input a number"))
if a>b and a>c:
    print (a, "is the largest number")
elif b>a and b>c:
    print (b, "is the largest number")
elif c>a and c>b:
    print (c, "is the largest number")
else: 
    print ("Please make sure the numbers you enter are different!")