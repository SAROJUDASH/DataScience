#Dictonary -Dictonaries are used to store data values in key:value pairs
#They are unordered,mutable(changable) and don't allows duplicate keys
info = {
    "name" : "Saroj Udash",
    "subjects" : ["Java", "Html", "CSS","c#"],
    "topics" : ("set", "tuple" ,"dict"),
    "class" : "Bachelor",
    "address" : "Bansbari,ktm"
}
print(info)
print(type(info))
print(info["name"])
print(info["subjects"])
print(info["topics"])
info["name"] = "Sugam" #overwrite
print(info)
info["caste"] = "Shrestha" #add
print(info)

#Nested Dictionary
college = {
    "name" : "Lumbini",
    "faculty" :{
        "+2" : ["Science", "Management", "Law"],
        "bachelor" : ("BCA", "BBS", "BHM")
    },
    "address" : "Chabahil"
}
print(college)
print(type(college))
print(college["faculty"])


#Dictionary methods
#clear()  -Removes all the elements from the dictionary
info.clear()
print(info)

#copy()	 -Returns a copy of the dictionary
x = info.copy()
print(x)

#get()	-Returns the value of the specified key
print(info.get("class"))
a = info.get("topics")  #returns the key according to value
print(a)


#keys()	 -Returns a list containing the dictionary's keys
#returns all keys
# m = info.keys()
# info["age"] = 23
# print(m)

print(info.keys())
print(list(info.keys()))


#values() -Returns a list of all the values in the dictionary
print(info.values())
print(tuple(info.values()))


#items() -Returns a list containing a tuple for each key value pair
#returns all (key,val) pairs as tuples
print(info.items())
print(list(info.items()))

# m = list(info.items())
# print(m[4])


#update() -Updates the dictionary with the specified key-value pairs
# info.update({"city" : "Kathmandu"})
# print(info)

new_dict = { "city" : "Pokhara"}
info.update(new_dict)
print(new_dict)