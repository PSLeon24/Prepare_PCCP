L = [i for i in range(0, 31)]
idx = -1
lower = 0
upper = len(L) - 1


def binary_search(L, x):
    global idx, lower, upper
    while lower <= upper:
        mid = (lower + upper) // 2
        if L[mid] == x:
            idx = mid
            return idx
        elif L[mid] < x:
            lower = mid + 1
        else:
            upper = mid - 1
    return -1


print(binary_search(L, 17))
print(binary_search(L, 37))
