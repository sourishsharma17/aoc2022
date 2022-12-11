x=open("11in.txt","r").read()

from collections import defaultdict as dd

x=x.split("\n\n")


t=dd(list)
o={}
p={}
q={}



c=dd(int)


for i in x:
    i=i.splitlines()
    a=int(i[0][-2])
    b=i[1].split(": ")
    for ii in b[1].split(", "):
        t[a].append(int(ii))

    o[a]=" ".join(i[2].split()[-2:])
    p[a]=int(i[3].split()[-1])
    q[a]=(int(i[4][-1]),int(i[5][-1]))



for ii in range(20):
    for i,r in t.items():
        for rr in r:
            c[i]+=1
            a=rr
            a=eval(f"{a} {o[i]}")
            a=a//3
            if a%p[i]==0:
                t[q[i][0]].append(a)
            else:
                t[q[i][1]].append(a)
        t[i]=[]


a=sorted(c.values())
print(a[-1]*a[-2])



















