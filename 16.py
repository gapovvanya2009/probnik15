def F(n):
    if n % 2 == 0:
        return F(n/2)+3
    else:
        if n % 3 == 0:
            return F(n/3)+2
        else:
            return 0
for n in range(1, 1000000000000000000):
    if F(n) == 65:
        print(n)
        break