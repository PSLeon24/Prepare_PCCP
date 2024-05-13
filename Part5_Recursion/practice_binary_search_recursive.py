def binsearch(L, x, lower, upper):
    if lower > upper:
        return -1
    mid = (lower + upper) // 2
    if L[mid] == x:
        return mid
    elif L[mid] < x:
        return binsearch(L, x, mid + 1, upper)
    else:
        return binsearch(L, x, lower, mid - 1)


L = [i for i in range(0, 31)]
print(binsearch(L, 17, 0, len(L) - 1))
print(binsearch(L, 37, 0, len(L) - 1))
