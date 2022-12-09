N = int(input())
A = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열을 담을 메모이제이션
dp = [A[0]]

for num in A[1:]:
    # dp 에 가장 마지막으로 저장된 값보다 수가 크다면, 부분 수열에 추가함
    if dp[-1] < num:
        dp.append(num)
    # 그렇지 않은 경우, 이분 탐색을 통해 어떤 부분부터 교체해야 하는지 파악.
    else:
        start, end = 0, len(dp)
        # 이분 탐색을 통해 시간 복잡도를 낮춤 (0(n) = n log n)
        while start < end:
            mid = (start + end) // 2
            # 중간 인덱스의 값이 현재 수보다 작을 경우, 시작 범위 감소
            if dp[mid] < num:
                start = mid + 1
            # 중간 인덱스의 값이 현재 수와 같거나 클 경우, 끝 범위 감소
            else:
                end = mid
        # 이분 탐색이 끝난 후, 교체해야 할 인덱스의 값을 덮어 씌움.
        dp[end] = num
print(len(dp))