import sys
from collections import deque

case = int(sys.stdin.readline())
for _ in range(case):
    # 함수 처리에 필요한 데이터를 인계 받음
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    # 배열처럼 보이는 문자열 중에서, 요소들만 indexing을 통해 추출하여 새로운 deque 생성
    # 앞 뒤 괄호를 제외한 나머지 문자열을 추출한 후, split() 함수로 쉼표를 기준 삼아 문자열 분할.
    # 만약 n이 0이라면 (빈 배열) indexing이 불가하므로 빈 deque를 생성하여 할당시킴
    arrStr = sys.stdin.readline().strip()[1:-1].split(',')
    arr = deque(arrStr) if n > 0 else deque()
    # 에러가 났는지를 검사해주는 is_error 변수 생성
    # reverse 횟수를 세는 reverse_cnt 변수 생성 (잦은 reverse() 로 인한 시간 초과)
    reverse_cnt, is_error = 0, False
    for func in p:
        if func == 'R':
            reverse_cnt += 1
        elif func == 'D':
            if len(arr) == 0:
                is_error = True
                print('error')
                break
            else:
                # 뒤집는 횟수가 짝수라면, 결국 같으므로 왼쪽의 수를 뺌
                if reverse_cnt % 2 == 0:
                    arr.popleft()
                # 뒤집는 횟수가 홀수라면, 좌우가 반전되므로 오른쪽의 수를 뺌
                else:
                    arr.pop()
    # error 가 검출되었는지를 먼저 판별해야 함
    if not is_error:
        # 만약 뒤집어야 하는 횟수가 홀수라면 배열을 뒤집어야 하므로 reverse() 실행.
        if reverse_cnt % 2 == 1:
            arr.reverse()
        string = '[' + ",".join([str(i) for i in arr]) + ']'
        print(string)

