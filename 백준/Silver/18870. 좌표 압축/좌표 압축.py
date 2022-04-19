import sys
n = int(sys.stdin.readline())
data, newData = list(map(int, sys.stdin.readline().split())), {}
# data를 set으로 변경하여 중복을 없애고, 이를 정렬하여 작은 수부터 오게 함
# 그런 후 다시 정렬된 set을 list로 변경하여 index를 구할 수 있도록 함.
rank = 0
for number in sorted(set(data)):
    newData[number] = rank
    rank += 1

result = []  
for point in data:
    result.append(newData[point])
print(*result)