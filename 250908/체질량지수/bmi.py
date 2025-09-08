N = input().split()
h, w = int(N[0]), int(N[1])
b = 10000 * w / h / h
print(int(b))
if (b>=25):
    print("Obesity")