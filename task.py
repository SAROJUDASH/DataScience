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

#Task6: Implement all the list method
a = [1,2,4,7.8,9,9,7,"Saroj","Udash",123,[1,2,3.3,4.5]]
print(a)
print(type(a))

#1. append() -Adds an element at the end of the list
a.append("Hello")
print(a)

#2. count() -Returns the number of elements with the specified value
print(a.count(9))

#3. index()  -Returns the index of the first element with the specified value
b = a.index(123)
print(b)
#Get the fist element of the list
#Indexing always start from 0
print(a[2])
print(a[10])


#4. slicing() -Create a new subset list from the original list
b = a[0:9]  # -The end value is always exclusive(The end value is not sliced)
#a. Start to ending slicing
print(b)
print(type(b))

#b. end slicing
c = a[:4]
print(c)

#c. start slicing
d = a[4:]
print(d)

#d. middle slicing
e = a[3:9]
print(e)

#e. positive index with step
f = a[::3]
print(f)

#f. negative index
print(a[-1])
print(a[-5])

#g. negative index with step
print(a[-1:-5:-1])
print(a[-5:-1:1])


#5. insert()	-Adds an element at the specified position
a.insert(2,"Today")
print(a)

#6. pop()	-Removes the element at the specified position
a.pop(4)
print(a)

#7. remove()	-Removes the item with the specified value
a.remove(4)
print(a)

#8. reverse()	-Reverses the order of the list
a.reverse()
print(a)


#Task7:  Implement all the indexing and slicing in string also
#indexing
name = "Saroj"
print(name[1])
print(name[4])
print(name[0])

#slicing
hello = name[1:3]

#a. start to ending slicing
print(hello)
print(type(hello))

#b. end slicing
hi = name[:4]
print(hi)

#c. start slicing
hee = name[1:]
print(hee)

#d middle slicing
hlo = name[1:4]
print(hlo)

#e positive index with step
hoo = name[::2]
print(hoo)

#f. negative index
print(name[-1])
print(name[-3])

#g. negative index with step
print(name[-1:-4:-1])
print(name[-3:-1:1])

#Task 8: Create a list of usernames input a username from the user check if the username is present in the list or not
usernames = ["Saroj", "Roman", "Samir", "Santosh","Bibek"]
user = input("Enter a username:")
if user in usernames:
    print("Username found in the list")
else:
    print("Username not found in the list")


#Task 9: Create a dictionary of usernames and passwords, extract all the usernames from the dictionary 
#and input username from the user and check if the username is present in the extracted list of usernames.
info = {
    "saroj" : "Sar123",
    "sunil" : "S12unil",
    "roman" : "r012an",
    "samir" : "saa45mir",
    "surya" : "s98urya32"
}
usernames = list(info.keys())
print(usernames)

user = input("Enter a username:")
if user in usernames:
    print("Username present in the dictionary.")
else:
    print("Username not present in the dictionary.")



# Task 10: Create a simple calculator system using Elif
num_1 = float(input("Enter first number:"))
num_2 = float(input("Enter second number:"))
oper = input("Enter operation (+, -, *, /,%): ")
if oper == "+":
    print("Result", num_1 + num_2)
elif oper =="-":
    print("Result", num_1 - num_2)
elif oper =="*":
    print("Result", num_1 * num_2)
elif oper =="/":
    print("Result", num_1 / num_2)
elif oper =="%":
    print("Result", num_1 % num_2)
else:
    print("Invalid operation")



#Task 11:Make a complete register and login system using dictationary

credentials = {
    "saroj" : "Saroj123"
}

choice = input("Enter 1 for Register, 2 for login:")

if choice == "1":
    username = input("Enter a username:")
    if username in credentials:
        print("Username already exists.")
    else:
        password = input("Enter a password:")
        credentials.update({username : password})
        print("Registration successfull.")
elif choice == "2":
    username = input("Enter a username:")
    password = input("Enter a password:")
    if username in credentials and credentials.get(username) == password:
        print("Login Successfully.")
    else:
        print("Login failed.")

else:
    print("Invalid choice.")
            

#Task 11:WAP to find the greatest number among three number, number is given by user
num_1 = float(input("Enter first number:"))
num_2 = float(input("Enter second number:"))
num_3 = float(input("Enter third number:"))

if num_1 > num_2 and num_1 > num_3:
    print(f"{num_1} is the greatest number.")
elif num_2 > num_1 and num_2 > num_3:
    print(f"{num_2} is the greatest number.")
else:
    print(f"{num_3} is the greatest number.")

