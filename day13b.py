x=open("13in.txt","r").read().replace("\n\n","\n").splitlines()
x.append("[[2]]")
x.append("[[6]]")



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


from copy import deepcopy as dp
xx=dp(x)
x=dp([])

while dp(x) != dp(xx):

    x=dp(xx)
    xx=dp([])
    for i in range(0,len(x),2):
        a,b=x[i:i+2]
        a,b=eval(a),eval(b)

        y=l(a,b)

        if y==1:
            xx.append(x[i])
            xx.append(x[i+1])
        else:
            xx.append(x[i+1])
            xx.append(x[i])

    x=dp(xx)
    xx=dp([])
    xx.append(x[0])
    for i in range(1,len(x)-1,2):
        a,b=x[i:i+2]
        a,b=eval(a),eval(b)

        y=l(a,b)

        if y==1:
            xx.append(x[i])
            xx.append(x[i+1])
        else:
            xx.append(x[i+1])
            xx.append(x[i])
    xx.append(x[-1])


print(xx.index("[[2]]"))
print(xx.index("[[6]]"))
print((xx.index("[[2]]")+1)*(xx.index("[[6]]")+1))



















