import copy
numbers=[1,2,3,4,5]

print(id(numbers))
# With id(numbers) you can
#
numbers[2]=True
print(id(numbers))
message="Hello World"
print(id(message))
a="hello"
print("a=",id(a))
a="hello"
print("a=",id(a))
# message[3]='p'
# The above statement leads to:
# TypeError: 'str' object does not support item assignment
# What does work is:
message=message[:3] + 'p' + message[4:]
print(id(message))
# here we create a new object and assign it to the same pointer (pointer is variable, pointing to an object)
# we did not change the existing object
print (message)
message="Hello World".upper()
print(message)
message.lower() #did not work
print(message)
message=message.lower() #does work
print(message)

print(numbers)
print(id(numbers))
numbers.pop()
print(numbers)
print(id(numbers))


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("=============== NOW THE REALLY WEIRD STUFF =================================")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

alist=[[1,2],[3,4]]
shallow_copy_alist=alist.copy() #This is a shallow copy
deep_copy_alist=copy.deepcopy(alist) #This is a deepcopy
print("alist:", alist)
print("shallow_copy_alist", shallow_copy_alist)
print("do shallow_copy_alist point to alist: ", shallow_copy_alist is alist)
print("do alist have the same elements as the shallow_copy_alist", shallow_copy_alist == alist)
shallow_copy_alist[0][0]=8 #Changing the shallow-copied list. Would that change the original?
print("shallow_copy_alist:", shallow_copy_alist)
print("alist:", alist) # INTERESTING FACT !!!! THE alist CHANGED AFTER CHANGING THE shallow_copy_alist!!!!

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ Conclusion, the shallow copy ONLY changes the outer-list, not the internal-lists!!! +"
      "")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


print("deep_copy_alist", deep_copy_alist) # HOWEVER, THE DEEP-COPIED LIST DID NOT CHANGE
print("do deep_copy_alist point to alist: ", deep_copy_alist is alist)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("=============== Slicing creates a shallow copy too =========================")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
