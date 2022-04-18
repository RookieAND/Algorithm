import sys
import collections

n = int(sys.stdin.readline())
commands = [tuple(sys.stdin.readline().split()) for _ in range(n)]
deque = collections.deque()

for cmd in commands:
    if cmd[0] == "push_front":
        deque.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        deque.append(cmd[1])
    elif cmd[0] == "pop_front":
        if len(deque) > 0:
            print(deque[0])
            deque.popleft()
        else:
            print(-1)
    elif cmd[0] == "pop_back":
        if len(deque) > 0:
            print(deque[len(deque)-1])
            deque.pop()
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(deque))
    elif cmd[0] == "empty":
        print(1 if len(deque) == 0 else 0)
    elif cmd[0] == "front":
        print(deque[0] if len(deque) > 0 else -1)
    elif cmd[0] == "back":
        print(deque[len(deque)-1] if len(deque) > 0 else -1)