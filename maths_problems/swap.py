#swap numbers using four diffrent ways
#1.using third variable
#2.using arithamtic operation that is addition and substraction
a=int(input("Enter the number: "))
b=int(input("Enter the second number: "))
print(f"Before swap a is {a} b is {b}")
a=a+b
b=a-b
a=a-b
print(f"After swap a is {a} b is {b}")