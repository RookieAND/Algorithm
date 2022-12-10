import sys

read = sys.stdin.readline
sudoku, blank = [], []

# 스도쿠 판과 공백이 담긴 좌표 값을 선별하여 저장.
for row in range(9):
    sudoku.append(list(map(int, read().strip())))
    for col in range(9):
        if sudoku[row][col] == 0:
            blank.append((row, col))

def check_sudoku(y, x, num):
    # 1번 (가로 줄) 의 조건이 유효한지 판별.
    for row in range(9):
        if sudoku[row][x] == num:
            return False
    # 2번 (세로 줄) 의 조건이 유효한지 판별
    for col in range(9):
        if sudoku[y][col] == num:
            return False
    # 3번 (3 x 3) 의 조건이 유효한지 판별
    for row in range(3):
        for col in range(3):
            if sudoku[(y // 3) * 3 + row][(x // 3) * 3 + col] == num:
                return False
    return True

# 빈 칸이 담긴 좌표에 대한 탐색을 진행.
def solve_sudoku(idx):
    # 모든 빈칸에 대한 탐색이 종료되었다면, 프로그램을 종료해야 함.
    if idx == len(blank):
        for i in range(9):
            print(*sudoku[i], sep="")
        sys.exit(0)
    # 그렇지 않을 경우 1 ~ 10 까지 숫자를 대입하면서 계산 시작.
    ny, nx = blank[idx]
    for num in range(1, 10):
        if check_sudoku(ny, nx, num):
            # 숫자를 넣을 수 있는 경우, 이를 대입하고 다음 좌표 탐색
            sudoku[ny][nx] = num
            solve_sudoku(idx + 1)
            # 그렇지 않을 경우 값을 초기화 하여 이전의 좌표로 돌아감.
            sudoku[ny][nx] = 0

solve_sudoku(0)
