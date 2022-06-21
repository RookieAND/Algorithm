import sys
sys.setrecursionlimit(10 ** 5)

read = sys.stdin.readline
N = int(read())
matrix = [list(map(int, read().split())) for _ in range(N)]

result = {-1: 0, 0: 0, 1: 0}


def divide(x, y, n):
    value = matrix[y][x]
    for loc_y in range(y, y + n):
        for loc_x in range(x, x + n):
            if matrix[loc_y][loc_x] != value:
                # 여기서부터는 분할을 진행하므로, 카운트하지 않아야 함.
                for len_y in range(3):
                    for len_x in range(3):
                        divide(x + len_x * (n // 3), y + len_y * (n // 3), n // 3)
                return

    result[value] += 1
    return


divide(0, 0, N)
print(*(result[-1], result[0], result[1]), sep='\n')