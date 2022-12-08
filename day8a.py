x=open("8in.txt","r").read()


x=[[int(r) for r in i]for i in x.splitlines()]


v=set()

for i in range(len(x)):
    m=-1
    for ii in range(len(x[i])):
        if x[i][ii]>m:v.add((ii,i))
        m=max(m,x[i][ii])

for i in range(len(x)):
    m=-1
    for ii in range(len(x[i])-1, -1,-1):
        if x[i][ii]>m:v.add((ii,i))
        m=max(m,x[i][ii])


for i in range(len(x[0])):
    m=-1
    for ii in range(len(x)):
        if x[ii][i]>m:v.add((i,ii))
        m=max(m,x[ii][i])




for i in range(len(x[0])):
    m=-1
    for ii in range(len(x)-1,-1,-1):
        if x[ii][i]>m:v.add((i,ii))
        m=max(m,x[ii][i])



print(len(v))









