import sys

n, m = map(int, sys.stdin.readline().split())
password_dict, result = {}, []
# 각 사이트 별 비밀번호를 key-value 형식으로 dict에 저장한다.
for _ in range(n):
    site, password = sys.stdin.readline().split()
    password_dict[site] = password
# 해당 사이트의 비밀번호를 dict 에서 불러와 result에 저장한다.
for _ in range(m):
    result.append(password_dict[sys.stdin.readline().strip()])
print(*result, sep="\n")