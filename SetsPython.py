#Set DataType -Set DataType is also a mutable datatype enclosed with {}.The index in set datatype is not fixed
students = {"Ram", "Shyam", "Hari", "Rohan","Sandip"}
players = {"Sugam","Hari", "Saroj","Rohan", "Yubaraj"}
print(type(students))
print(len(students))


#add()	-Adds an element to the set
students.add("Bibek")
print(students)

#clear()  -Removes all the elements from the set
students.clear()
print(students)

#difference()  -Returns a set containing the difference between two or more sets
print(students.difference(players))
print(players.difference(students))

#discard()	 -Remove the specified item
students.discard("Rohan")
print(students)

#intersection() 	-Returns a set, that is the intersection of two other sets
print(students.intersection(players))

#isdisjoint()	 -Returns whether two sets have a intersection or not
disjoint = students.isdisjoint(players)
print(disjoint)

#issubset()	 -Returns True if all items of this set is present in another set
subset = students.issubset(players)
print(subset)

#issuperset()	-Returns True if all items of another set is present in this set
superset = students.issuperset(players)
print(superset)


#pop()	 -Removes an element from the set
players.pop()
print(players)


#remove()	-Removes the specified element
# players.remove("Sugam")
# print(players)


#symmetric_difference()	-Returns a set with the symmetric differences of two sets
y = students.symmetric_difference(players)
print(y)


#union()  -Return a set containing the union of sets
print(students.union(players))


#update()	-Update the set with the union of this set and others
students.update(players)
print(students)