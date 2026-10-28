sent=input("Enter a sentence ")
count=0
for i in range(len(sent)-1,-1,-1):
  if sent[i]!=' ':
    count+=1
  else:
    break
print(count)  