import sys
n, m = map(int, sys.stdin.readline().split())
cant_hear, cant_see = set(), set()

# 생성된 두 개의 set 에 순차적으로 사람들의 이름을 담음
for _ in range(n):
    cant_hear.add(sys.stdin.readline().strip())
for _ in range(m):
    cant_see.add(sys.stdin.readline().strip())

# 두 개의 set의 교집합이 바로 듣보잡이므로 교집합 연산 수행
cant_seeAndHear = cant_see & cant_hear
print(len(cant_seeAndHear))

# 그 후 해당 set을 사전 순으로 정렬하여 출력시킴
for people in sorted(cant_seeAndHear):
    print(people)
