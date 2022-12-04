x = open("4in.txt", "r").read().splitlines()


t = 0


for i in x:

    a,b=i.split(",")

    aa, aaa = [int(r) for r in a.split("-")]
    bb, bbb = [int(r) for r in b.split("-")]

    if bbb >= aa >= bb or aaa >= bb >= aa:t+=1



print(t)


