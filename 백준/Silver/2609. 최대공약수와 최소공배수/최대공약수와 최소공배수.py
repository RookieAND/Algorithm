import sys

a, b = map(int, sys.stdin.readline().split())
def sep_number(num):
    d, result = 2, []
    while num >= d:
        if num % d == 0:
            num = num // d
            result.append(d)
        else:
            d += 1
    return result

sep_a, sep_b = sep_number(a), sep_number(b)
G, L = 1, 1
for n in sorted(set(sep_a).union(set(sep_b))):
    # 공통된 인수가 있으면, 최대 공약수와 최소 공배수 케이스를 추가.
    if n in sep_a and n in sep_b:
        G *= n ** min(sep_a.count(n), sep_b.count(n))
        L *= n ** max(sep_a.count(n), sep_b.count(n))
    else:
        L *= n ** max(sep_a.count(n), sep_b.count(n))
print(G, L)