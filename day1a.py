t=0
x=open("1in.txt", "r").read().split("\n\n")

for i in x:
    t=max(t,sum([int(r) for r in i.splitlines()]))

print(t)
