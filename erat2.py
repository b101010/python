def erat(n):

    a = [True]*n
    b = []

    for j in range(2, n):
        if a[j]:
            for i in range(j*2, n, j):
                a[i] = False

    for (num, item) in enumerate(a):
        if item and num >= 2:
            b.append(num)          

    return b

print(erat(100))    