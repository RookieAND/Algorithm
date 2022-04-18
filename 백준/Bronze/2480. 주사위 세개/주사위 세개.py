result = list(map(int, input().split()))
result.sort()
result2Set = list(set(result))
for i in result2Set:
    result.remove(i)
if len(result) == 0:
    print(result2Set[2] * 100)
elif len(result) == 1:
    print(result[0] * 100 + 1000)
else:
    print(result[0] * 1000 + 10000)
