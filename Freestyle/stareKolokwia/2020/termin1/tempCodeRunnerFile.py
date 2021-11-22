l_copy = [None]*(m+1-l)
    r_copy = [None]*(r-m)

    for i in range(l,m+1):
        l_copy[i] = T[i]

    for j in range(m+1,r+1):
        r_copy[j] = T[j]