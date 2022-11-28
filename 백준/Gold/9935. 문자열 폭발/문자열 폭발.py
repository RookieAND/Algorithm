import sys

read = sys.stdin.readline
sentence = read().rstrip()
boom = list(read().rstrip())

stack = []
for word in sentence:
    stack.append(word)
    # 폭발 문자열의 가장 마지막 단어를 추가했을 때, 폭발 문자열이 만들어지는지 확인.
    if len(stack) >= len(boom) and word == boom[-1] and stack[-len(boom):] == boom:
            del stack[-len(boom):]
sentence = "".join(stack)
print('FRULA' if not sentence else sentence)