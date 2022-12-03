x = open("3in.txt", "r").read().splitlines()

t = 0

from string import ascii_uppercase, ascii_lowercase

for i in x:
    a,b=i[:len(i)//2], i[len(i)//2:]

    for r in a:
        if r in b:
            if r.islower():t+=ascii_lowercase.index(r)+1
            else:t+=ascii_uppercase.index(r)+27
            break


print(t)


