def hanoi(n, start, end, temp):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, temp, end)
    print(start, end)
    hanoi(n - 1, temp, end, start)


print(hanoi(3, 1, 3, 2))
