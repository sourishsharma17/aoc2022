x=open("6in.txt", "r").read()


a=list(x[:14])

for i in range(14,len(x)):
    if len(set(a))==14:print(i);break
    a.pop(0)
    a.append(x[i])




