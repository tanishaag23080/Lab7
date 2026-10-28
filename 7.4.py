sent=input("Enter a sentence ")
sent=sent.lower()
for char in "abcdefghijklmnopqrstuvwxyz":
  if char not in sent:
    print("Not a pangram")
    break
else:
  print("Is a pangram")