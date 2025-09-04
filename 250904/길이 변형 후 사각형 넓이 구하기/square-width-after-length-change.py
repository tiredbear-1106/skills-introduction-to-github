a = input().split()
l, h = int(a[0]), int(a[1])
l += 8
h *= 3
print(l, h, l*h, sep='\n')