import sys

n = int(sys.stdin.readline().strip())
commands, stack = [tuple(sys.stdin.readline().split()) for _ in range(n)], []

for command in commands:
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) > 0:
            print(stack[len(stack)-1])
            stack.pop()
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(0 if len(stack) > 0 else 1)
    elif command[0] == "top":
        print(stack[len(stack)-1] if len(stack) > 0 else -1)