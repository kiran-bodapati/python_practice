list1=[1,1,1]
list2=[1,1,1]
list3=[1,1,1]
list4=[list1,list2,list3]
print(list4)
a=input("enter the position where you want to hide money:")
b=int(a[0])
c=int(a[1])
d=list4[b-1]
d[c-1]='x'

print(f"{list1},{list2},{list3}")
