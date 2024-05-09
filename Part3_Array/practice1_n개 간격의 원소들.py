num_list = [4, 2, 6, 1, 7, 6]
n = 4

result = []
for i in range(0, len(num_list), n):
    result.append(num_list[i])

print(result)
