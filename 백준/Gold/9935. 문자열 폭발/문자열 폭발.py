import sys

read = sys.stdin.readline
sentence = read().rstrip()
boom = list(read().rstrip())

stack = []
for word in sentence:
    stack.append(word)
    if len(stack) >= len(boom) and word == boom[-1] and stack[-len(boom):] == boom:
        del stack[-len(boom):]
sentence = "".join(stack)
print('FRULA' if not sentence else sentence)