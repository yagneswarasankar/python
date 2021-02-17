#This program will remove only one element . As this program is intended to delete
# the first occrrence in the entire list


list = ["git","C++","C++","svc", "maven"]
ele = "C++"
print(list)
for element in list:
    if(element == ele):
        list.remove(element)

print(list)

