def sl(m,n):
    s = n
    for i in range(0, m):
        s = s + pow(n,0.5)
        n = pow(n,0.5)
    print("%.2f"%s)
sl(2,16)


