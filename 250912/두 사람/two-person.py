a_age, a_gen = input().split()
a_age = int(a_age)

b_age, b_gen = input().split()
b_age = int(b_age)

if a_age>=19 and a_gen=="M":
    print("1")
else:
    if b_age>=19 and b_gen=="M":
        print("1")
    else:
        print("0")