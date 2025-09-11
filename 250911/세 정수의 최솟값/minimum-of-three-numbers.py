N = input().split()
a, b, c = int(N[0]), int(N[1]), int(N[2])

if a<b:
    if a<c:
        print(a)
    else :
        print(c)
else:
    if b<c:
        print(b)
    else:
        print(c)