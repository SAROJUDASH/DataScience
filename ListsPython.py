#Task: Implement all the list method

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