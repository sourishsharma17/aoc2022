t=[]
x=open("1in.txt", "r").read().split("\n\n")

for i in x:
    t.append(sum([int(r) for r in i.splitlines()]))


t=sorted(t)
print(sum(t[-3:]))
