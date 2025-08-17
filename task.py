#task1: WAP to print your name
print("Saroj udash")

#task2: Input a fav player name and print it
name = input("Enter your favorite player name:")
print(name)

#task3: Input for every data type we discussed and print it
num = int(input("Enter any integer:"))
print(num)
name = input("Enter any string:")
print(name)
num1 =float(input("Enter any floating number:"))
print(num1)



#task4: Ask input of two numbers from the user and perform operations on those numbers or values
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print("Add:", a+b)
print("Sub:", a-b)
print("Multiply:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)
print("Power:", a**b)
print("Lowcase:", a//b)
print("Greater than:", a>b)
print("Less than:", a<b)
print("Greater than or equals to:", a>=b)
print("Less than or equals to:",a<=b)
print("Equal:",a==b)
print("Not equal:",a!=b)



# Task 5: Ask user a string and print if b is in that string or not. Do use in and not in
name = input("Enter your name:")
if "b" in name:
    print("b is present.")
else:
    print("b is absent.")
