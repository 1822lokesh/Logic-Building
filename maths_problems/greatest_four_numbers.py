# ask the users to four numbers 
a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))
d=int(input("Enter a fourth number: "))
# this line checks the  b and c and d with a using "bitwise and"
if a > b and a > c and a > d:
    print("A is greater")
# this line checks the c and d with b
elif b > c and b > d:
    print("B is greater")
# this line checks d with c
elif c > d:
    print("C is greater")
else:
    print("D is greater")