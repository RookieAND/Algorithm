result, data = int(input()), list(map(int, input().split()))
for num in data:
    if num == 1:
        result -= 1
        continue
    else:
        for i in range(2, num):
            if num % i == 0:
                result -= 1
                break
print(result)