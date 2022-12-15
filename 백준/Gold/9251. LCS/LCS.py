A, B = input().rstrip(), input().rstrip()

# dp[i] = A 문자열 중 i번째 인덱스까지의 부분 문자열 내에서, 가장 긴 LCS의 길이.
# 단, 1차원 배열을 캐시로 사용하기 때문에 이전의 값을 메모이제이션하여 갱신해야 함.
dp = [0] * len(B)

for i in range(len(A)):
    # matched : A와 B 문자열을 순회하면서 매칭된 글자의 최대 수량
    matched = 0
    for j in range(len(B)):
        # 현재 메모이제이션 된 값보다 누적 변수가 작을 경우, 이를 맞춰줌
        if matched < dp[j]:
            matched = dp[j]
        # 만약 글자가 일치한다면, 현재 누적 변수에서 1을 더한 값을 저장함.
        elif A[i] == B[j]:
            dp[j] = matched + 1

print(max(dp))