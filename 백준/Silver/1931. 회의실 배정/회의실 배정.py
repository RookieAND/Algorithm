import sys

n = int(sys.stdin.readline())
conferences = []
for _ in range(n):
    start, end = tuple(map(int, sys.stdin.readline().split()))
    conferences.append((start, end))
# 두 번의 정렬을 통해, 끝나는 시간이 빠른 순서대로 먼저 정렬을 진행해야 함 (빨리 끝날수록 좋음)
# 만약 종료 시간이 같다면 시작 시간이 빠를수록 좋으므로, 시작 순서대로 정렬을 추가 진행함.
conferences.sort(key=lambda x: x[0])
conferences.sort(key=lambda x: x[1])

result, current_end = 0, 0
# 회의가 일찍 끝난 순서대로, 시작을 일찍 한 순서대로 강의 목록를 순회함.
for start, end in conferences:
    # 해당 회의의 시작 시간이 현재 회의가 끝난 시간과 같거나 큰지를 판별
    # 만약 맞다면, 새로운 회의를 추가하고 끝나는 시간을 업데이트 함.
    if start >= current_end:
        current_end = end
        result += 1
print(result)