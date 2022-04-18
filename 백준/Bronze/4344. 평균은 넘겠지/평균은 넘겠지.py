N, data = int(input()), []
for _ in range(0, N):
    data.append(list(map(int, input().split())))
for case in data:
    pct = len([i for i in case[1:] if i > sum(case[1:]) // case[0]]) / (len(case) - 1) * 100
    print("{0:.3f}%".format(pct))