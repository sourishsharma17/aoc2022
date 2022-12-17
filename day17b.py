x=open("17in.txt", "r").read().rstrip()


r=(((0,0),(1,0),(2,0),(3,0)),((0,1),(1,1),(2,1),(1,0),(1,2)),((0,0),(1,0),(2,0),(2,1),(2,2)),((0,0),(0,1),(0,2),(0,3)),((0,0),(0,1),(1,0),(1,1)))

s=0

v=[(i,0) for i in range(7)]

v=set(v)

yy=0
p=set()
hh=()

j=[0]
y=[0]

k=[0]*7

from copy import deepcopy as dp

for i in range(1000000000000):
    a=r[i%len(r)]
    b=[]
    for aa in a:
        b.append(aa[0]+2)
        b.append(aa[1]+4+yy)

    while 1:
        c=0
        if x[s%len(x)]==">":l=1
        else:l=-1
        for ii in range(0,len(b),2):
            b[ii]+=l
        if -1 in b:c=1
        if 7 in b:c=1
        for ii in range(0,len(b),2):
            if (b[ii],b[ii+1])in v:c=1

        if c:
            for ii in range(0,len(b),2):
                b[ii]-=l
        c=0
        s+=1
        for ii in range(1,len(b),2):
            b[ii]-=1
        for ii in range(0,len(b),2):
            if (b[ii],b[ii+1])in v:c=1
        if c:
            for ii in range(1,len(b),2):
                b[ii]+=1
            break

    for ii in range(1,len(b),2):
        yy=max(yy,b[ii])
        k[b[ii-1]]=max(k[b[ii-1]],b[ii])
    kk=min(k)
    kkk=dp(k)
    for ii in range(len(kkk)):
        kkk[ii]-=kk
    for ii in range(0,len(b),2):v.add((b[ii],b[ii+1]))
    if (tuple(kkk),s%len(x),i%len(r))== ((6, 6, 6, 6, 0, 1, 0), 828, 0):
        print(i,i-j[-1])
        j.append(i)
        print(yy,yy-y[-1])
        y.append(yy)
        break
    if (tuple(kkk),s%len(x),i%len(r)) in p and 0:
        print(i)
        print((tuple(kkk),s%len(x),i%len(r)))
        break
        print(i-j[-1])
        j.append(i)

    p.add((tuple(kkk),s%len(x),i%len(r)))
print(yy)













