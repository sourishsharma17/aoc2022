x=open("13in.txt","r").read().split("\n\n")



p=1
t=0

def l(a,b):
    for i in range(min(len(a),len(b))):
        if isinstance(a[i],int) and isinstance(b[i],int):
            if a[i]<b[i]:return 1
            if a[i]>b[i]:return -1
        elif isinstance(a[i],list) and isinstance(b[i],list):
            y=l(a[i],b[i])
            if y!=0:return y
        elif isinstance(a[i],int) and isinstance(b[i],list):
            y=l([a[i]],b[i])
            if y!=0:return y
        elif isinstance(a[i],list) and isinstance(b[i],int):
            y=l(a[i],[b[i]])
            if y!=0:return y
    if len(a)<len(b):return 1
    if len(a)>len(b):return -1
    return 0



for i in x:
    a,b=[eval(r) for r in i.splitlines()]

    y=l(a,b)

    if y==1:t+=p
    p+=1

print(t)
    




















