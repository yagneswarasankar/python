import random

list = ["git","svc", "maven"]
#"append" will add an element in the end.
#list.append(x)
#Add an item to the end of the list. Equivalent to a[len(a):] = [x].
list.append("sbt")
print(list)

#"extend" will add list of elements to an existing list
#list.extend(iterable)
#Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
newlist = ["scala","python","r","java"]
list.extend(newlist)
print(list)

#"insert" will insert an email at the specified location in a list
# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to
# insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x)
# is equivalent to a.append(x).
#at first location
ele = "C++"
list.insert(0,ele)
print(list)
#From end
list.insert(-1,ele)
print(list)
#At Last
list.insert(len(list),ele)
print(list)
#at a specific location let us say 6th position (As index starts from 6)
list.insert(6-1,ele)
print(list)
# remove the first occurrence of an element from a list
#list.remove(x)
#Remove the first item from the list whose value is equal to x.
# It raises a ValueError if there is no such item.
list.remove(ele)
print(list)

#to remove an element from a spcific index
#list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified,
# a.pop() removes and returns the last item in the list. (The square brackets around the i in
# the method signature denote that the parameter is optional, not that you should type square
# brackets at that position. You will see this notation frequently in the Python Library Reference.)
##** Again the index starts from 0 so it will delete the
list.pop(3)
print(list)







