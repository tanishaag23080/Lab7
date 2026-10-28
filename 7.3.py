sent=input("Enter a sentence ")
word=input("Enter a word ")
s=word in sent
print(s)
if s==True:
  print("Sentence contain word")
else:
  print("Sentence don't contain word")
c=sent.count(word)
print(c)