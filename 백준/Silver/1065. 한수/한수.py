def count():
    num = int(input())
    if num < 100:
        count = num
    else:
        count = 99
        for i in range(100, num + 1):
            a, b, c = i // 100, (i % 100) // 10, i % 10
            if a + c == b * 2:
                count += 1
    print(count)
count()