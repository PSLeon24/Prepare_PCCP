L = [1, 2, 3, 3, 4, 3, 5, 6, 2]

indexes = []

while 3 in L:
    indexes.append(L.index(3))
    L[L.index(3)] = 0

print(indexes)
