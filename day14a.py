x=open("14in.txt","r").read().splitlines()

q=set()

for i in x:
    i=i.split(" -> ")
    for ii in range(len(i)-1):
        a,b=i[ii],i[ii+1]
        a,b=a.split(","),b.split(",")
        print(a,b)
        for xx in range(min(int(a[0]),int(b[0])),max(int(b[0])+1,int(a[0])+1)):
            for yy in range(min(int(a[1]),int(b[1])),max(int(b[1])+1,int(a[1])+1)):
                q.add((xx,yy))


s=len(q)
print(s)
from time import sleep
sleep(0)

while 1:
    #print(len(q))
    a,b=500,0
    c=0
    while 1:
        c+=1
        if c > 10000:print(len(q)-s);break
        if (a,b+1) not in q:
            b+=1
            continue
        else:
            if (a-1,b+1) not in q:
                a-=1
                b+=1
                continue
            elif (a+1,b+1) not in q:
                a+=1
                b+=1
                continue
        q.add((a,b))
        break











