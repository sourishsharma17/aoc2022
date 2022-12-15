x=open("15in.txt","r").read().splitlines()

t={}
y={}

for i in x:
    i=i.replace(",","").replace(":","").replace("x=","").replace("y=","")
    i=i.split()

    a,b,c,d=[int(r) for r in [i[2],i[3],i[-2],i[-1]]]
    t[(a,b)]=(c,d)
    y[(a,b)]=abs(a-c)+abs(b-d)
    

from collections import defaultdict as dd
from copy import deepcopy as dp
q=dd(list)

for i,r in y.items(): 
    a=i[0]-r#minx
    b=i[0]+r#maxx
    c=i[1]-r#miny
    d=i[1]+r#maxy
    for ii in range(c,d+1):
        aa=r-abs(i[1]-ii)
        f,g=i[0]-aa,i[0]+aa
        #f->minx at y=ii
        q[ii].append((f,g))
        """
        n=[]

        for h in q[ii]:
            if h[0]<=f<=h[1] and h[0]<=g<=h[1]:
                #del f,g
                n.append(h)
                continue
            if h[0]<=f<=h[1]:
                #del f,h[1]
                n.append((h[0],g))
                continue

            if h[0]<=g<=h[1]:
                #del g,h[0]
                n.append(f,h[1]))
                continue
        """

def mi(arr):
    arr.sort(key=lambda x: x[0])
    index = 0
    for i in range(1, len(arr)):
        if (arr[index][1] >= arr[i][0]):
            arr[index][1] = max(arr[index][1], arr[i][1])
        else:
            index = index + 1
            arr[index] = arr[i]
    a=[]
    for i in range(index+1):
        a.append(arr[i])
    return a

from time import sleep
for i,r in q.items():
    r=[list(k) for k in r]
    n=mi(r)
    """
    nn=[]
    n=dp(r)
    while n != nn:
        nn=dp(n)
        n=[]
        for a in range(len(nn)):
            for b in range(a+1,len(nn)):
                if a[0]<=b[0]<=a[1] and a[0]<=b[1]<=a[1]:
                    n.append(nn[a]kkkkkkkk
    """



    if len(n) > 1:
        print(n)
        print(i)
        n=sorted(n)
        print(((n[0][1]+1)*4000000)+i)

        sleep(2)












