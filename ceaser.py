import random
print("\t\t\t\t\t Crypt Your Data ")
t=(input("Enter the string :- "))
s=list(t.lower())
l=list(chr(x) for x in range(97,123))
r=random.randint(1,25)
for i in range(len(s)):
    if(s[i]==' '):
        s[i]=chr(random.randint(32,64))
    else:
        x=s[i]
        x=(l.index(x)+r)%26+1
        s[i]=l[x-1]
s=''.join(s)
s=s+str(r)
print(s)
input("Press Anything to Close")
