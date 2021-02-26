#Program 1
# num_Players = 10
# print(f"Number of Players: {num_Players}")
# # To change the global variable inside a function
# def mutateglobalVariableFunction():
#     global num_Players
#     print(f"Inside the function value is : {num_Players}")
#     num_Players += 1
# #Now the values is 11 as the global value is mutated
# print("calling insideFunction: ")
# mutateglobalVariableFunction() #This will print 10 as the value is not been mutated yet (before printing)
# print(f"Again came out and the vaue now is :{num_Players} ")  #11
# num_Players+= 1
# print(num_Players) #12 as we added one to it

# Number of Players: 10
# calling insideFunction:
# Inside the function value is : 10
# Again came out and the vaue now is :11
# 12

#Program 2
gl_var = 12
def localFunction():
    gl_var = 15
    print(f"gl_var value inside the function :{gl_var}")
    (f"hash code of local Variable : {id(gl_var)}")
    return gl_var,id(gl_var)
print(f"Outside the function : {gl_var}")
print("Comparing local and global variables : ")
print(f"hash code of global Variable : {id(gl_var)}")
gl_local_var,hash_code = localFunction()
print(f"gl_local_var: {gl_local_var}")
print(f"hash_code of local vriable : {id(gl_var)}")



