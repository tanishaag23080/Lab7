word=input("Enter a word ")
rev=""
for char in range (len(word)-1,-1,-1):
  rev+=word[char]
print(rev)