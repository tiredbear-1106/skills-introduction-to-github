A = input().split()
B = input().split()
am, ae, bm, be = int(A[0]), int(A[1]), int(B[0]), int(B[1])

if am>bm and ae>be:
    print('1')
else:
    print('0')