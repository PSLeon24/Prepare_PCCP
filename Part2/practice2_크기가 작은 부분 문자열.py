def solution(t, p):
    n = len(p)
    numbers = []
    for i in range(len(t) - n + 1):
        numbers.append(t[i : i + n])

    numbers = list(map(int, numbers))
    p = int(p)

    answer = 0
    for i in range(len(numbers)):
        if numbers[i] <= p:
            answer += 1

    return answer


t1 = "3141592"
p1 = "271"
t2 = "500220839878"
p2 = "7"
print(solution(t1, p1))
print(solution(t2, p2))
