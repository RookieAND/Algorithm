import sys

read = sys.stdin.readline
R, C = map(int, read().split())
# 입력 받은 대문자 알파벳을 0 ~ 26 사이의 숫자로 변환. (ord(A) = 65)
matrix = [list(map(lambda x: ord(x) - 65, read().rstrip())) for _ in range(R)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

max_move = 1
words = [False] * 26 # A ~ Z 알파벳 갯수만큼 List 제작

def dfs(loc_y, loc_x, move):
    global max_move
    max_move = max(max_move, move)
    for dir_y, dir_x in direction:
        ny, nx = dir_y + loc_y, dir_x + loc_x
        if 0 <= ny < R and 0 <= nx < C and not words[matrix[ny][nx]]:
            words[matrix[ny][nx]] = True
            dfs(ny, nx, move + 1)
            words[matrix[ny][nx]] = False

# 가장 첫 지점의 경우 항상 경유하므로 True로 변환.
words[matrix[0][0]] = True
dfs(0, 0, max_move)
print(max_move)
