x=open("10in.txt","r").read().splitlines()



t=0
q=0
xx=1

y=[]
for i in range(6):
    p=["#"]*40
    y.append(p)

y=["."]*240
l=0
ii=0


for i in x:
    if i =="noop":
        if ii%40 in (xx-1,xx,xx+1):
            y[ii]="#"
        ii+=1
    else:
        a,b=i.split()
        b=int(b)

        if ii%40 in (xx-1,xx,xx+1):
            y[ii]="#"
        ii+=1
        if ii%40 in (xx-1,xx,xx+1):
            y[ii]="#"

        ii+=1

        xx+=b


for i in range(6):
    print("".join(y[i*40:i*40+40]))
    







