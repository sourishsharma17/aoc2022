x = open("3in.txt", "r").read().splitlines()

t = 0

from string import ascii_uppercase, ascii_lowercase

for i in range(0,len(x),3):

    a,b,c=x[i],x[i+1],x[i+2]

    a,b,c=set(a),set(b),set(c)
    a=a.intersection(b)
    a=a.intersection(c)
    a=list(a)
    r=a[0]
    if r.islower():t+=ascii_lowercase.index(r)+1
    else:t+=ascii_uppercase.index(r)+27


print(t)


