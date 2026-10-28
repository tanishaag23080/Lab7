n=int(input())
count=0
c1,c2,c3,c4,c5=0,0,0,0,0
while n!=-1:
    n=int(input())
    if n>=1 or n<=10:
        count+=1
        if n==1 or n==2:
            c1+=1
        elif n==3 or n==4:
            c2+=2 
        elif n==5 or n==6:
            c3+=1 
        elif n==7 or n==8:
            c4+=1 
        else:
            c5+=1
    else:
        print("invalid input")
p1=f'{(c1/count)*100:.2f}'
p2=f'{(c2/count)*100:.2f}'
p3=f'{(c3/count)*100:.2f}'
p4=f'{(c4/count)*100:.2f}'
p5=f'{(c5/count)*100:.2f}'

print('1-2:',"#"*c1,p1)
print('3-4:',"#"*c2,p2)
print('5-6:',"#"*c3,p3)
print('7-8:',"#"*c4,p4)
print('9-10:',"#"*c5,p5)