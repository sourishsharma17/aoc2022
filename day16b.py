x=open("16in.txt","r").read().splitlines()

t={}
y={}

for i in x:
    i=i.replace("="," ").replace(",","").replace(";","")
    i=i.split()

    y[i[1]]=int(i[5])
    t[i[1]]=i[10:]


from collections import deque as de

# min opened curr tot
q=de([(0,(),"AA","AA",0)])
v=set()
w=0

l=0
for i in y.values():
    if i !=0:l+=1
print(l)
u=sum(y.values())
print(u)
from time import sleep
sleep(0)

from collections import defaultdict as dd
h=dd(int)
print(y)
while q:
    a,b,c,cc,d=q.popleft()
    #f,ff=1,1
    #print(a)
    #print(b)
    #print(a,b,c,d)
    if a==26:w=max(w,d);print(w);continue
    if len(b)==l:w=max(w,(26-a)*u+d);print(w);continue
    if (b,c,cc) in v:continue
    if (b,cc,c) in v:continue
    v.add((b,c,cc))
    v.add((b,cc,c))
    if a > 10:
        if d<8.5*(h[a]//10):continue

    dd=d
    for i in b:
        dd+=y[i]


    h[a]=max(h[a],d)
    if y[c]!=0:
        if c not in b:
            bb=tuple(list(b)+[c])

            if y[cc]!=0:
                if cc not in b and cc != c:
                    bbb=tuple(list(bb)+[cc])
                    q.append((a+1,bbb,c,cc,dd))
                    if cc != "AA":continue

            for i in t[cc]:
                q.append((a+1,bb,c,i,dd))
            #if c != "AA":continue

    if y[cc]!=0:
        if cc not in b:
            bb=tuple(list(b)+[cc])


            for i in t[c]:
                if i in b:continue
                #if len(b)==l-1:i=c
                q.append((a+1,bb,i,cc,dd))

            if cc != "AA":continue

    for i in t[c]:
        for ii in t[cc]:
            #if ii==i:continue
            #if i in b:continue
            #if len(b)==l-1:i=c
            q.append((a+1,b,i,ii,dd))











