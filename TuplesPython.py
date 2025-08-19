#Tuples -Tuples is a immutable data type in python that wraps the element in ()
#Tuple is used to creates the constants
# tup = (1,2,3,4,5,4,3,2)
# print(tup)
# print(type(tup))  #check type
# print(tup[3])
# print(tup[5])
# print(tup[7])
# print(tup[1:5])
# print(tup[:5])
# print(tup[4:])

#Tuple methods
#count()	-Returns the number of times a specified value occurs in a tuple
# tup = (1,2,3,4,5,4,3,2,2,2)
# tuple = tup.count(2)#4
# print(tuple)

#index()	-Searches the tuple for a specified value and returns the position of where it was found
tup = (1,2,3,4,5,4,3,2,2,2)
tuple = tup.index(5) #4
print(tuple)

#How to convert used to tuple 
list1 = [1,2,3,"Saroj", "Udash"]
tup = tuple(list1)
print(type(tup))