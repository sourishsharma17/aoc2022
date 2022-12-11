x=open("9in.txt","r").read().splitlines()
from copy import deepcopy as dp



v=set()

ww=[]
qq=[]
for i in range(10):
    ww.append([0,0])
    qq.append([0,0])
q,w=[0,0],[0,0]
v.add(tuple(w))


for i in x:
    a,b=i.split()
    b=int(b)

    for ii in range(b):

        for iii in range(1,10):
            q=dp(ww[iii-1])
            w=dp(ww[iii])

            if iii==1:
                if a=="U":
                    q[1]-=1
                if a=="D":
                    q[1]+=1
                if a=="R":
                    q[0]+=1
                if a=="L":
                    q[0]-=1

            #if q[0] != w[0] and q[1] != w[1] and (w[0] == q[0]-1 or w
            if abs(q[0]-w[0])+abs(q[1]-w[1]) == 3:
                if q[0]==w[0]-2:
                    w[0]-=1
                    w[1]+=q[1]-w[1]
                if q[0]==w[0]+2:
                    w[0]+=1
                    w[1]+=q[1]-w[1]
                if q[1]==w[1]-2:
                    w[1]-=1
                    w[0]+=q[0]-w[0]
                if q[1]==w[1]+2:
                    w[1]+=1
                    w[0]+=q[0]-w[0]


            elif abs(q[0] - w[0]) > 1 or abs(q[1] - w[1]) > 1:
                if q[0]==w[0]-2:
                    w[0]-=1
                if q[0]==w[0]+2:
                    w[0]+=1
                if q[1]==w[1]-2:
                    w[1]-=1
                if q[1]==w[1]+2:
                    w[1]+=1

            if iii==9:v.add(tuple(w))
            #qq[iii]=dp(q)
            ww[iii]=dp(w)
            ww[iii-1]=dp(q)
            print(q,w)




print(len(v))




