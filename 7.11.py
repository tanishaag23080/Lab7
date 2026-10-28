a=input()
upper=0
lower=0
alpha=0
digit=0
sp=0
for ch in a:
    if ch.isdigit():
        digit+=1
    elif ch.isalpha():
        alpha+=1
        if ch.isupper():
            upper+=1
        elif ch.islower():
            lower+=1
    elif not ch.isspace():
        sp+=1
print('upper:',upper)
print('lower:',lower)
print('alpha:',alpha)
print('digit:',digit)
print('sp:',sp)