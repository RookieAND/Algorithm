import sys

n, m = map(int, sys.stdin.readline().split())
pokemon_dict = {}
# n번에 걸쳐 순서대로 포켓몬을 Dict에 저장함 (입력 받은 순서대로 번호를 매김)
# 숫자 : 이름, 이름 : 숫자 와 같이 key-value를 2회에 걸쳐 저장해야 함 (시간 초과)
for i in range(1, n+1):
    pokemon = sys.stdin.readline().strip()
    pokemon_dict[i] = pokemon
    pokemon_dict[pokemon] = i
for j in range(m):
    # 입력이 숫자로 들어왔는지, 문자로 들어왔는지를 판별해야 함
    question = sys.stdin.readline().strip()
    # 입력 받은 값이 숫자일 경우, 해당 숫자에 맞는 value를 출력
    if question.isdigit():
        answer = pokemon_dict[int(question)]
    # 그렇지 않을 경우. 이진 탐색을 통해 해당 포켓몬의 key를 탐색
    else:
        answer = pokemon_dict[question]
    print(answer)