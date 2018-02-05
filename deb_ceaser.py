print("\t\t\t\t\t Decrypt Your Data ")
t=(input("Enter the string :- "))
j=list(t.lower())
l=list(chr(x) for x in range(97,123))
if(ord(j[-2])<=57):
    r=[str(ord(j[-2])-48),j[-1]]
    r=''.join(r)
    r=int(r)
    j.pop(-2)
else:
    r=int(j[-1])
j.pop(-1)
for i in range(len(j)):
    if(j[i] in list(chr(x) for x in range(32,65))):
        j[i]=' '
    else:
        x=j[i]
        x=(l.index(x)-r)%26
        j[i]=l[x]
j=''.join(j)
print(j)
input("press anything to close ")
