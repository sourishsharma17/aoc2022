x=open("7in.txt", "r").read().splitlines()

from collections import defaultdict as dd


y=dd(list)
yy={}
u=[]

for i in x:
    if i[0] =="$":
        if i[2]=="c":
            if i[5]==".":
                u.pop()
            else:#in
                u.append(i[5:])
        else:#ls
            pass
    else:#ls output
        if i[:4] == "dir ":
            y["".join(u)].append("".join(u)+i.split()[1])
        else:#file
            y["".join(u)].append("".join(u)+i.split()[1])
            yy["".join(u)+i.split()[1]]=int(i.split()[0])



t=0
def d(tt,c):
    global t
    if c in yy.keys():return yy[c]
    for i in y[c]:
        tt += d(0,i)
    if tt <= 100000:t+=tt
    return tt

d(0,"/")

print(t)








