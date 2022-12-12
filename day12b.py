x=open("12in.txt","r").read().splitlines()
x=[list(i) for i in x]


from collections import deque as de


for i in range(len(x)):
    for r in range(len(x[0])):
        if x[i][r] == "S":a=(i,r);x[i][r]="a"
        if x[i][r] == "E":bb=(i,r);x[i][r]="z"

t=1e99

for ii in range(len(x)):
    for rr in range(len(x[0])):
        if x[ii][rr]!="a":continue
        q=de([(ii,rr,0)])
        v=set()

        while q:
            a,b,c=q.popleft()
            if (a,b) == bb:t=min(t,c);break
            if (a,b)in v:continue
            v.add((a,b))
            if c >= t:continue
            for i in range(a-1,a+2):
                for r in range(b-1,b+2):
                    if len(x) >i>0 and len(x[0])>r>0 and (i==a or r==b):
                        if ord(x[i][r]) <= ord(x[a][b])+1:q.append((i,r,c+1))





print(t)

