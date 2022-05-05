import sys

n = int(sys.stdin.readline())

result = []
for _ in range(n):

    stack, is_wrong = [], False
    vps = sys.stdin.readline().strip()
    for v in vps:
        if v == '(':
            stack.append(v)
        # 만약 닫는 괄호가 왔다면, 현재 스택에서 1개를 제거함.
        elif v == ')':
            try:
                stack.pop()
            # 단, 현재 stack이 비어있다면 틀린 괄호이므로, 예외 처리
            except IndexError:
                is_wrong = True
                break

    if len(stack) == 0 and not is_wrong:
        result.append('YES')
    else:
        result.append('NO')

print(*result, sep="\n")