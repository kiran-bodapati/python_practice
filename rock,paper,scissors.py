import random
a=int(input("enter your choice:"))
if a>2 or a<0:
     print("wrong input")

b=random.randint(0,2)
print(b)
if a==b:
        print("draw")
elif a==2 and b==0:
        print("b wins")
elif a==0 and b==2:
        print("a wins")
elif a>b:
        print("a win")
elif b>a:
        print("b win")
    
 
