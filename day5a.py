x=open("5in.txt","r").read()

x,y=x.split("\n\n")

x,y=x.splitlines(),y.splitlines()


q=[""]*9


for i in range(len(x)-2,-1,-1):
    for r in range(1,len(x[0]), 4):
        if x[i][r].isupper():q[r//4]+=x[i][r]



for i in y:
    a,b,c,d,e,f=i.split()

    b,d,f=int(b),int(d),int(f)
    print(b,d,f)
    d,f=d-1,f-1

    for r in range(b):
        q[f]+=q[d][-1]
        q[d]=q[d][:-1]


t=""
for i in q:
    t+=i[-1]

print(t)


