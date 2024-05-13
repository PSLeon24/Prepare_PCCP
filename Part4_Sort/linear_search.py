def linear_search(L, x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1


L = [3, 5, 1, 2, 4, 0]
print(linear_search(L, 5))
print(linear_search(L, 10))
