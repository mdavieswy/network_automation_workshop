mylist = [4, "mike", 29.99, True]
for thing in mylist:
    print (thing)

print("====")
for index, element in enumerate(mylist):
    print(index, element)

print("====")  
mylist.insert(2,"new")

print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
#print(mylist[4])
dir(mylist[3])
mylist.append("bang")
print(dir(mylist[4]))
print(mylist[4])
print(mylist[5])

print("====")  

for index, element in enumerate(mylist):
    print(index, element)  

