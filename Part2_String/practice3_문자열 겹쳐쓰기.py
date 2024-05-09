def solution(my_string, overwrite_string, s):
    answer = ""
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string) :]
    return answer


my_string = "Program29b8UYP"
overwrite_string = "merS123"
s = 7

print(solution(my_string, overwrite_string, s))
