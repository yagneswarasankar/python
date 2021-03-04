##From the site https://towardsdatascience.com/60-questions-to-test-your-knowledge-of-python-lists-cca0ebfa0582



# ###
# ###Q1. Check if a list contains an element
# ###
# list = ["girija","sankar",,"Sri","Hari","Prasad","Sita","Rama","Sastry"]
# lower_list = []
# for ele in list:
#     lower_list.append(ele.lower())
# inp = raw_input("Enter the element to check: ").lower()
# if inp in lower_list:
#     print("Given element  exists: ")
# else:
#     print"does not exists"

# ####
# ##Q2 Traverse two lists at the same time and fetching the elements
# ####
# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]
# animal_name = zip(name,animal)
# print(type(animal_name))
# print(type(animal_name[0]))

# ###
# #Q3. Is List is mutable
# ###
# list3 = [1]
# print(id(list3),':',list3)
# list3.append(5)
# list3.extend([6,7])
# print(id(list3),':',list3)

# ####
# #Q4. Is a string mutable
# #####
# ## No a String is immutable
# str  = "Girija"
# print(id(str))
# str += "Duvvuri"
# print(id(str))

# ###
# ##Q5. Does a list need to be homogeneous?
# ###
#
# #A list can be hetero genious and can contain different types of elements
# list5 = [23,"Girija",(34,32,5)]
# print(list5)

####
##Q6. What is the difference between append and extend
####

# ## "append" will add an element at the end of the list
# list6 = [3,4,2]
# list6.append(34)
# print(list6)
#
# ## "extend"  will add multiple elements
# list6.extend([43,54])
# print(list6)

# ##
# #Q7 Does python lists store values or pointers
# ##
# a = 1
# b = 2
# list73 = [1,2,3]
# print("id(a): "+ str(id(a)))
# print("id(b): "+ str(id(b)))
# print("id(list73): "+ str(id(list73)))
# print("id(list73[0]):" + str(id(list73[0])))


###
# #Q8 What does “del” do?
#del removes an item from a list given its index.

list = [2,3,4,3]
print(list[:2])
print(list[1:])



