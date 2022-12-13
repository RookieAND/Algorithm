import sys
sys.setrecursionlimit(10 ** 6)

steps = list(map(int, input().split()))

# dp[idx][lp][rp] : idx 번째 스텝을 진행한 후, 왼발이 lp에 오른발이 rp에 있을 때 드는 최소의 힘.
dp = [[[-1] * 5 for _ in range(5)] for _ in range(len(steps))]


def move(before, after):
    if before == after:
        return 1
    elif before == 0:
        return 2
    elif abs(after - before) % 2 == 0:
        return 4
    else:
        return 3


def solve(idx, left_pos, right_pos):
    global dp
    # 입력 받은 스텝보다 인덱스가 더 큰 경우, 0을 리턴 (재귀의 마지막)
    if idx >= len(steps) - 1:
        return 0
    # 이미 이전에 메모이제이션된 값이 있다면 이를 리턴.
    if dp[idx][left_pos][right_pos] != -1:
        return dp[idx][left_pos][right_pos]

    # 왼발을 뻗었을 경우, 혹은 오른발을 뻗었을 경우 더 적은 힘이 드는 값으로 저장.
    # 마지막 스텝까지 재귀를 반복하다가 끝에 도달하면, 기존에 더해진 힘을 통해 역으로 산술하는 방식.
    dp[idx][left_pos][right_pos] = min(solve(idx + 1, steps[idx], right_pos) + move(left_pos, steps[idx]), solve(idx + 1, left_pos, steps[idx]) + move(right_pos, steps[idx]))
    return dp[idx][left_pos][right_pos]

print(solve(0, 0, 0))