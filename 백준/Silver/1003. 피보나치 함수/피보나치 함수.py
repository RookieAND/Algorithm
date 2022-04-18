import sys

N = int(sys.stdin.readline())
case = [int(sys.stdin.readline()) for _ in range(N)]
dp_cnt0 = [1, 0, 1]
dp_cnt1 = [0, 1, 1]

def fibonacci(N):
    length = len(dp_cnt0)
    if num >= length:
        for i in range(length, num+1):
            dp_cnt0.append(dp_cnt0[i-1] + dp_cnt0[i-2])
            dp_cnt1.append(dp_cnt1[i - 1] + dp_cnt1[i - 2])
    print(f"{dp_cnt0[num]} {dp_cnt1[num]}")
            
for num in case:
    fibonacci(num)