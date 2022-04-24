import sys

n = int(sys.stdin.readline())

# a는 높은 수부터 낮은 수대로 내림차순, b는 낮은 수부터 높은 수대로 오름차순을 진행
# b에서 가장 낮은 수와 a에서 가장 높은 수를 곱해야 하므로, 결국 두 list를 정렬해야 함.
a = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
b = sorted(list(map(int, sys.stdin.readline().split())))

result = 0
for i in range(n):
    result += a[i] * b[i]
print(result)