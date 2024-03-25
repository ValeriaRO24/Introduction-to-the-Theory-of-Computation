def  mergesort(L):
    """Returns a list  representing L in  sorted  order.
    """
    n = len(L)
    if n == 0 or n == 1:
        return L
    else:
        L1 = mergesort(L[0:n//2])
        L2 = mergesort(L[n//2:n])
        return  combine(L1, L2)


def  combine(L1, L2):
    """Combines  two  sorted  lists  L1 and L2
    into a single  sorted  list , and  returns.
    """
    i1 , i2 = 0, 0
    n1 = len(L1)
    n2 = len(L2)
    L = []
    while i1 < n1 and i2 < n2:
        if L1[i1]  <= L2[i2]:
            L.append(L1[i1])
            i1 += 1
        else:
            L.append(L2[i2])
            i2 += 1
    if i1 < n1:
        L = L + L1[i1:n1]

    if i2 < n2:
        L = L + L2[i2:n2]
    return L

print(mergesort([3, 4, 1, 12, 3, 56, 2]))
