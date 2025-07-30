mylist =[1,2,4,'python',3.14,True]

print(mylist)
print("list length",len(mylist))
print("First element:", mylist[0])
print("Last element:", mylist[-1])
print("range of list:", mylist[3:])
mylist.remove(4)
mylist.append("java")
print(mylist)
mylist[0]=200
print("Updated list:", mylist)