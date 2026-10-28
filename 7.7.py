word=input("Enter a word ")
a=""
for i in range (len(word)-1,-1,-1):
    a+=word[i]
if a==word:
    print("Pallindrome")
else:
    print("Not a pallindrome")