dictio={'one': 1}
atuple=(1,2)
mylist=["martin", "Gorren"]
foo={8,4,7,2,21,1,2,3,True,"Hello",1.34,atuple}
x=len(foo)
print("length: ",x)
for x in foo:
    print("item: ", x)
print("This is foo", foo)
print(foo.pop())
print(foo)
