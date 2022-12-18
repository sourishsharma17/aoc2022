x=open("18in.txt","r").read().splitlines()


v=set()

t=0

for i in x:
    a,b,c=[int(r) for r in i.split(",")]

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





