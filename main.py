l = 6
for i in range(l, 0, -1):
    print(" " * (l - 1 - i) + "*" * (1 + i * 2))
else:
    l = 6
    for i in range(l):
        print(" " * (l - 1 - i) + "*" * (1 + i * 2))