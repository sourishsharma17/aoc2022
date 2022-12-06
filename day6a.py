x=open("6in.txt", "r").read()


a=list(x[:4])

for i in range(4,len(x)):
    if len(set(a))==4:print(i);break
    a.pop(0)
    a.append(x[i])




