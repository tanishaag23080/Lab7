A=input()
b=[]
word=""
inverted=''
for i in range(len(A)):
    if A[i]=="-":
        b.append(word)
        word=''
        continue
    else:
        word+=A[i]
b.append(word)
for j in range(len(b)):
    for k in range(j+1,len(b)):
        if b[j]>b[k]:
            b[j],b[k]=b[k],b[j]
for i in range(len(b)):
    if i==len(b)-1:
        inverted+=b[i]
    else:
        inverted+=b[i]+'-'
print(inverted)
