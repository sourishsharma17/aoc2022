x=open("15in.txt","r").read().splitlines()

t={}
y={}

for i in x:
    i=i.replace(",","").replace(":","").replace("x=","").replace("y=","")
    i=i.split()

    a,b,c,d=[int(r) for r in [i[2],i[3],i[-2],i[-1]]]
    t[(a,b)]=(c,d)
    y[(a,b)]=abs(a-c)+abs(b-d)
    

q=[i[0] for i in t.values()]
q,w=min(q),max(q)

print(q,w)
v=set()

g=10
g=2000000

for i in range(q*10,w*10):
    for ii,rr in y.items():
        if abs(ii[0]-i)+abs(ii[1]-g) <= rr:
            if (i,g) not in t.values():
                v.add((i,g))

print(len(v))











