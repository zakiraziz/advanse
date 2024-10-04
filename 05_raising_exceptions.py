a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey uor program is not meant to divide numbers by zero ")

else:
    print("The division a/b is {a/b}")