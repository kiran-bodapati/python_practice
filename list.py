row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
a=input("enter the position where you want to hide the money:")
b=int(a[0])
c=int(a[1])
d=matrix[b-1]
d[c-1]='x'
print(f"{row1}\n{row2}\n{row3}")

