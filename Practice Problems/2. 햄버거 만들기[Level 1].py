"""
1: 빵
2: 야채
3: 고기
즉, 1231 마다 answer += 1
"""


def solution(ingredient):
    answer = 0

    hambergers = []
    for i in ingredient:
        hambergers.append(i)
        if hambergers[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                hambergers.pop()
    return answer
