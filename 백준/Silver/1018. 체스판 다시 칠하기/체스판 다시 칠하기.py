import sys

m, n = map(int, sys.stdin.readline().split())
data, result = [list(sys.stdin.readline().strip()) for _ in range(m)], []

def check_paint(row, col):
    origin_W, origin_B = 0, 0
    for i in range(row, row+8):
        for j in range(col, col+8):
            if (i + j) % 2 == 0:
                if data[i][j] != 'W':
                    origin_W += 1
                else:
                    origin_B += 1
            else:
                if data[i][j] != 'B':
                    origin_W += 1
                else:
                    origin_B += 1
    result.append(min(origin_W, origin_B))

for row in range(0, m-7):
    for col in range(0, n-7):
        check_paint(row, col)
print(min(result))
