a = int(input())
b = int(input())
c = int(input())
result = str(a * b * c)
print(result.count("0"))
for i in range(1, 10):
    print(result.count(str(i)))
