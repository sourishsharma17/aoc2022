x=open("10in.txt","r").read().splitlines()



t=0
q=0
xx=1

for i in x:
    if i=="noop":
        q+=1
        if q in (20,60,100,140,180,220):
            t+=(q*xx)
    else:
        a,b=i.split()
        b=int(b)
        q+=1
        if q in (20,60,100,140,180,220):
            t+=(q*xx)
        q+=1
        if q in (20,60,100,140,180,220):
            t+=(q*xx)
        xx+=b

    
if q in (20,60,100,140,180,220):
    t+=(q*xx)

print(t)






