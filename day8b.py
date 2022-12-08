x=open("8in.txt","r").read()


x=[[int(r) for r in i]for i in x.splitlines()]

t=0

for i in range(len(x)):
    for r in range(len(x[0])):
        y=1

        o=0
        for ii in range(i+1,len(x)):
            if x[ii][r]<x[i][r]:o+=1
            else:o+=1;break
        y*=o
            

        o=0
        for ii in range(i-1,-1,-1):
            if x[ii][r]<x[i][r]:o+=1
            else:o+=1;break
        y*=o
 
        o=0
        for rr in range(r+1,len(x[0])):
            if x[i][rr]<x[i][r]:o+=1
            else:o+=1;break
        y*=o
  
        o=0
        for rr in range(r-1,-1,-1):
            if x[i][rr]<x[i][r]:o+=1
            else:o+=1;break
        y*=o

        t=max(y,t)

print(t)
