A, B = map(int, input().split())
AE = set(map(int, input().split()))
BE = set(map(int, input().split()))

print(len(AE | BE) - len(AE & BE))