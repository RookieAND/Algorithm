from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

# LIS : 모든 등가 수열 중 최대 길이를 가지는 경우를 저장하는 배열
LIS = [A[0]]
# LIS_IDX : 특정 인덱스의 수를 사용할 경우, 해당 숫자가 포함된 수열의 길이를 저장하는 배열.
# ex) (10, 1) 의 경우, 숫자 10이 들어간 수열의 최대 길이가 1이라는 의미.
LIS_IDX = [(A[0], 0)]

# 0번째 인덱스의 경우에 대한 결과는 이미 사전에 저장했으므로, 1번째부터 탐색 시작.
for num in A[1:]:
    # 만약 lis 배열 내 가장 마지막에 온 값이 더 크다면, 배열에 새로운 값을 추가.
    if LIS[-1] < num:
        LIS.append(num)
        LIS_IDX.append((num, len(LIS) - 1))
    # 그렇지 않을 경우 배열을 갱신해야 하므로, 중간에 삽입할 인덱스를 찾아야 함.
    else:
        insert_idx = bisect_left(LIS, num)
        LIS[insert_idx] = num
        LIS_IDX.append((num, insert_idx))


current_idx = len(LIS) - 1
result = []
# LIS_IDX 배열을 역으로 탐색하여, 현재 배열의 인덱스를 충족하는 값을 업데이트 함.
for num, num_idx in LIS_IDX[::-1]:
    if num_idx == current_idx:
        current_idx -= 1
        result.append(num)

print(len(result))
print(*result[::-1])