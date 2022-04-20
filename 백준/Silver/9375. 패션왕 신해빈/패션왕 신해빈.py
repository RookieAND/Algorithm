import sys

n, answer = int(sys.stdin.readline()), []
for _ in range(n):
    cloth_dict = {}
    # M번에 걸쳐 각 의류에 대한 정보를 입력 받아 Dict에 저장시킴.
    for i in range(int(sys.stdin.readline())):
        _, cloth = tuple(sys.stdin.readline().split())
        # 해당 의류가 Dict에 존재하지 않는다면, 새로운 key를 생성
        if cloth not in cloth_dict:
            cloth_dict[cloth] = 1
        # 그렇지 않을 경우 기존의 값에 1을 더함 (옷 종류 + 1)
        else:
            cloth_dict[cloth] += 1
    result = 1
    # 경우의 수 : (각 의류 별 수량 + 1) 을 전부 곱해주어야 함 (안 입는 경우 고려)
    for cloth in cloth_dict.keys():
        result *= (cloth_dict[cloth] + 1)
    # 모든 옷을 입지 않을 경우 (알몸인 상태) 를 고려하여 결과값에 1을 제외해야 함.
    answer.append(result - 1)
print(*answer, sep="\n")