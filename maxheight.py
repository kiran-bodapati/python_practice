a=input("enter the heights:")
b=a.split()
count=0
for i in b:
    count+=1

for i in range(0,count):
  b[i]=int(b[i])
print(b)
maximum=b[0]

for i in b:
    if maximum<i:
     maximum=i
print(f"the maximum number is:{maximum}")
    
    

