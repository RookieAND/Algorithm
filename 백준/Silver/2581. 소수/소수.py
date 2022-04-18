m, n = int(input()), int(input())
data = list(range(m, n+1))
for num in range(m, n+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                data.remove(num)
                break
    else:
        data.remove(num)
if len(data) == 0:
    print(-1)
else:
    print(sum(data))
    print(min(data))
