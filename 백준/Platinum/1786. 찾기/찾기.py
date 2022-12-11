import sys

read = sys.stdin.readline
T = read().rstrip()
P = read().rstrip()

# 이동경로 테이블 pi 생성
def make_table():
    # idx 개의 부분 문자열 내에서, 가장 긴 경계의 길이를 보관하는 배열 table
    table = [0] * len(P)
    # 이전의 분석에서 발생된 경계 (동일한 접두 / 접미사) 의 길이를 담은 변수 j
    j = 0
    # 부분 문자열의 길이를 1부터 패턴의 길이까지 분석하여 경계의 최대 길이 산출.
    for i in range(1, len(P)):
        # 양 끝의 문자열이 같지 않을 경우, 경계의 길이를 이전의 조사 값만큼 감소시킴.
        while j > 0 and P[i] != P[j]:
            j = table[j - 1]
        # 만약 문자열이 같을 경우, 경계 길이 값에 1을 더하고 현재 부분 문자열의 경계 값을 적용시킨다.
        if P[i] == P[j]:
            j += 1
            table[i] = j
    return table


def KMP():
    table = make_table()
    j = 0
    for i in range(0, len(T)):
        while j > 0 and T[i] != P[j]:
            j = table[j - 1]
        if T[i] == P[j]:
            if j == len(P) - 1:
                answer.append(i - len(P) + 2)
                j = table[j]
            else:
                j += 1

answer = []
KMP()
print(len(answer))
print(*answer)