import random
print("\t\t\t\t\t Crypt Your Data ")
t=(input("Enter the string :- "))
s=list(t.lower())
l=list(chr(x) for x in range(97,123))
d='cipher'
d=list(d)
k=0
for i in range(len(s)):
    if(s[i]==' '):
        s[i]=chr(random.randint(32,64))
    else:
        x=s[i]
        x=(l.index(x)+l.index(d[k%6]))%26+1
        s[i]=l[x-1]
        k=k+1
s=''.join(s)
print(s)
input("Press Anything to Close ")
