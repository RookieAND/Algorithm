import sys

N = int(sys.stdin.readline())
house_costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, len(house_costs)):
    house_costs[i][0] = min(house_costs[i-1][1], house_costs[i-1][2]) + house_costs[i][0]
    house_costs[i][1] = min(house_costs[i - 1][0], house_costs[i - 1][2]) + house_costs[i][1]
    house_costs[i][2] = min(house_costs[i - 1][0], house_costs[i - 1][1]) + house_costs[i][2]
print(min(house_costs[N-1]))