lst=[]
n=int(input("Enter integer"))
s=0
m=1
small=1000
for i in range(n):
    a=int(input("Enter list numbers"))
    s=s+a
    m=m*a
    lst.append(a)
    if a<small:
        small=a
print("Sum:",s)
print("Product:",m)
print(lst)
print("Smallest",smalls)
    
    


