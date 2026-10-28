word=input("Enter a word ")
num=int(input("Enter a number "))
caesar=""
for i in (word):
  a=ord(i)
  s=a+num
  caesar+=chr(s)
print(caesar)