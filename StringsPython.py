#String is a data type that stores a sequence of characters.
str1 = "Saroj"
str2 = "Udash"
final_str = str1 + " " +str2 #concatenation (+)
print(final_str)
print(len(final_str)) #Length of string


#STRING METHODS IN PYTHON
#index() -Returns the index of the element
#Get the fist element of the list
#Indexing always start from 0
names = "Mind_Risers"
print(names[0])
print(names[4])
print(names[9])
print(names.index("e"))


#capitalize()	Converts the first character to upper case
num1 = "hello everyone"
num = num1.capitalize()
print(num)


#count()	Returns the number of times a specified value occurs in a string
names = "Hello how are you?"
name = names.count("o")
print(name)


#replace()	Returns a string where a specified value is replaced with a specified value
names = "Hello how are you?"
name = names.replace("o","a")
print(name)


#strip() -Trim the string -Remove Whitespace
name = input("Enter your name:")
print(name)
print(name.strip)

#split()  -Returns the list of strings and we use seperator in split that is unique than other characters to separate sprit
string  = "Playing,Singing, Dancing, Coding, Reading"
print(string.split(","))

#slicing() -Specify the start index and the end index, separated by a colon, to return a part of the string.
name = "Saroj_Udash"
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
