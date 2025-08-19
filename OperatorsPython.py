#An operator is a symbol that performs a certain operation between operands.
a = int(input("Enter a number:"))
b = int(input("Enter a another number:"))

#Arithmetic operators
print("Arithmetic Operators:")
print("Add:",a+b)
print("Sub:", a-b)
print("Multiply:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)
print("Power:", a**b)

#Relational Operators
print("Relational operators:")
print("Equal:",a==b)
print("Not equal:",a!=b)
print("Greater than:", a>b)
print("Less than:", a<b)
print("Greater than or equals to:", a>=b)
print("Less than or equals to:",a<=b)

#Assignment Operators
print("Assignment Operators:")
x = 10
x += 10
print(x)

x -= 10
print(x)

x *= 10
print(x)

x /= 10
print(x)

x %= 10
print(x)

x **= 10
print(x)

#Logical Operators
print("Logical Operators:")
#NOT
if not 5>=7:
    print("True")
else:
    print("False")
#AND
if 4>3 and 7<8:
    print("True")
else:
    print("False")

#OR
if 4>3 or 7<8:
    print("True")
else:
    print("False")


#Identify Operators
print("Identify Operators:")
name = input("Enter your name:")
if "b" is name:
    print("b is present.")
else:
    print("b is absent.")


#Membership Operators
print("Membership Operators:")
names = input("Enter your favorite player name:")
if "a" in names:
    print("a is present.")
else:
    print("a is absent.")
