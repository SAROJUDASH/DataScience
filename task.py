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
