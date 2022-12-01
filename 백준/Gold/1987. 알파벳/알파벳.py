import sys

read = sys.stdin.readline
R, C = map(int, read().split())
matrix = [list(read().rstrip()) for _ in range(R)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_move = 1

def bfs():
    global max_move
    # y, x, 이동하면서 지나친 알파벳을 합친 문자열을 하나의 요소로 묶음
    # 시작은 (0, 0) 좌표부터 이므로 굳이 매개변수를 받지 않아도 됨.
    queue = {(0, 0, matrix[0][0])}
    while queue:
        ny, nx, words = queue.pop()
        # 지금까지 만나온 알파벳의 수량이 이동한 칸의 갯수와 같음.
        # 따라서 이를 기존의 최대 이동 거리와 비교하여 계산해야 함.
        max_move = max(max_move, len(words))
        for dir_y, dir_x in direction:
            my, mx = ny + dir_y, nx + dir_x
            if 0 <= my < R and 0 <= mx < C and matrix[my][mx] not in words:
                queue.add((my, mx, words + matrix[my][mx]))

bfs()
print(max_move)