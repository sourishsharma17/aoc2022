x=open("18in.txt","r").read().splitlines()


v=set()

t=0
q,w,e=100,100,100
qq,ww,ee=-5,-5,-5


for i in x:
    a,b,c=[int(r) for r in i.split(",")]
    q=min(q,a)
    w=min(w,b)
    e=min(e,c)
    qq=max(qq,a)
    ww=max(ww,b)
    ee=max(ee,c)

    v.add((a,b,c))

    for aa in range(a-1,a+2):
        if (aa,b,c) not in v: t+=1
        elif aa!=a:t-=1
    for bb in range(b-1,b+2):
        if (a,bb,c) not in v: t+=1
        elif bb!=b:t-=1
    for cc in range(c-1,c+2):
        if (a,b,cc) not in v: t+=1
        elif cc!=c:t-=1


print(t)

y=0

f=0
print(q,w,e)
print(qq,ww,ee)
z=[]
zz=[]
q,w,e=[i-1 for i in (q,w,e)]
qq,ww,ee=[i+1 for i in (qq,ww,ee)]

for a in range(q,qq+1):
    z.append([])
    zz.append([])
    for b in range(w,ww+1):
        z[-1].append([])
        zz[-1].append([])
        for c in range(e,ee+1):

            if (a,b,c) in v:f=1
            else:f=0
            z[-1][-1].append(f)
            zz[-1][-1].append(0)

            """
            if f==1:
                if (a,b,c) in v:
                    f=0
                    y+=0

            else:
                if (a,b,c) in v:
                    for aa in range(a-1,a+2,2):
                        for bb in range(b-1,b+2,2):
                            for cc in range(c-1,c+2,2):
                                if (aa,bb,cc) not in v:y+=1
                    f=1
                    y+=0
            if f==1:f=0;break
            """

print("--")
from copy import deepcopy as dp
from collections import deque as de

v=set()
q=de([(0,0,0)])

print(z)
while q:
    a,b,c=q.popleft()
    if (a,b,c)==(2,2,2):print("HH")
    if (a,b,c) in v:continue
    v.add((a,b,c))
    if z[a][b][c]==1:continue

    for aa in range(a-1,a+2,2):
        if len(z)>aa>-1:
            q.append((aa,b,c))

    for bb in range(b-1,b+2,2):
        if len(z[0])>bb>-1:
            q.append((a,bb,c))

    for cc in range(c-1,c+2,2):
        if len(z[0][0])>cc>-1:
            q.append((a,b,cc))



zz=set()
for a in range(len(z)):
    for b in range(len(z[0])):
        for c in range(len(z[0][0])):
            zz.add((a,b,c))
print(len(v))
print(len(zz))
zz=zz.difference(v)
print(zz)
print(z[1][1][1])

zz=tuple(zz)
y=0
for i in zz:
    a,b,c=i
    if z[a][b][c] == 1:continue
    for aa in range(a-1,a+2,2):
        if len(z)>aa>-1:
            if z[aa][b][c]==1:y+=1

    for bb in range(b-1,b+2,2):
        if len(z[0])>bb>-1:
            if z[a][bb][c]==1:y+=1

    for cc in range(c-1,c+2,2):
        if len(z[0][0])>cc>-1:
            if z[a][b][cc]==1:y+=1

print(y)
print(t-y)

print("---------___")



from time import sleep
sleep(10)



for a in range(len(z)):
    for b in range(len(z[0])):
        for c in range(len(z[0][0])):
            if zz[a][b][c]==6:y+=1
print(zz)

print(t-y*6)













