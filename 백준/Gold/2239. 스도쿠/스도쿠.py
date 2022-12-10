import sys

read = sys.stdin.readline
sudoku = [list(map(int, read().strip())) for _ in range(9)]

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

# 탐색 순서 => 가로 줄 탐색 후 다음 세로 줄로 이동하는 방식.
def solve_sudoku(y, x):
    # 만약 스도쿠 탐색이 종료되었다면, 프로그램을 종료해야 함.
    if y == 9:
        for i in range(9):
            print(*sudoku[i], sep="")
        sys.exit(0)
    # 만약 현재 위치에 이미 숫자가 작성되었다면, 다음 위치로 패스해야 함.
    elif sudoku[y][x] > 0:
        solve_sudoku(y + ((x + 1) // 9), (x + 1) % 9)
    # 그렇지 않을 경우 1 ~ 10 까지 숫자를 대입하면서 계산 시작.
    else:
        for num in range(1, 10):
            # 숫자를 넣을 수 있는 경우, 이를 대입함.
            if check_sudoku(y, x, num):
                sudoku[y][x] = num
                solve_sudoku(y + ((x + 1) // 9), (x + 1) % 9)
                # 백 트래킹 과정
                sudoku[y][x] = 0

solve_sudoku(0, 0)