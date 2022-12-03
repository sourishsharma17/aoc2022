x=open("2in.txt", "r").read().splitlines()

t=0
for i in x:
    i=i.split()

    if i[0]=="A":
        if i[1]=="X":t+=0;t+=3
        if i[1]=="Y":t+=3;t+=1
        if i[1]=="Z":t+=6;t+=2

    if i[0]=="B":
        if i[1]=="X":t+=0;t+=1
        if i[1]=="Y":t+=3;t+=2
        if i[1]=="Z":t+=6;t+=3


    if i[0]=="C":
        if i[1]=="X":t+=0;t+=2
        if i[1]=="Y":t+=3;t+=3
        if i[1]=="Z":t+=6;t+=1


print(t)
