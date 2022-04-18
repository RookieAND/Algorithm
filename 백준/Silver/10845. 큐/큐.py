import sys
import collections as collect

n = int(sys.stdin.readline().strip())
commands, queue = [tuple(sys.stdin.readline().split()) for _ in range(n)], collect.deque()

for command in commands:
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if len(queue) > 0:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif command[0] == "front":
        print(queue[0] if len(queue) > 0 else -1)
    elif command[0] == "back":
        print(queue[len(queue)-1] if len(queue) > 0 else -1)