l = 6
for i in range(l):
    for j in range(l):
        print("*", end="\t")
    print()
    if l > 0:
        print()
        l -= 1