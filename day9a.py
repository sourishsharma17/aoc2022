x=open("9in.txt","r").read().splitlines()




v=set()

q,w=[0,0],[0,0]
v.add(tuple(w))


for i in x:
    a,b=i.split()
    b=int(b)

    for ii in range(b):

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
                v.add(tuple(w))
            if q[0]==w[0]+2:
                w[0]+=1
                w[1]+=q[1]-w[1]
                v.add(tuple(w))
            if q[1]==w[1]-2:
                w[1]-=1
                w[0]+=q[0]-w[0]
                v.add(tuple(w))
            if q[1]==w[1]+2:
                w[1]+=1
                w[0]+=q[0]-w[0]
                v.add(tuple(w))


        elif abs(q[0] - w[0]) > 1 or abs(q[1] - w[1]) > 1:
            if q[0]==w[0]-2:
                w[0]-=1
                v.add(tuple(w))
            if q[0]==w[0]+2:
                w[0]+=1
                v.add(tuple(w))
            if q[1]==w[1]-2:
                w[1]-=1
                v.add(tuple(w))
            if q[1]==w[1]+2:
                w[1]+=1
                v.add(tuple(w))

            print(q,w)




print(len(v))




