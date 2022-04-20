import sys

m = int(sys.stdin.readline())
cmd_set = set()

for _ in range(m):
    command = sys.stdin.readline().strip().split()
    if len(command) == 1:
        if command[0] == "all":
            cmd_set = set([i for i in range(1, 21)])
        elif command[0] == "empty":
            cmd_set = set()
        continue
    else:
        cmd, num = command[0], command[1]
        num = int(num)
        
        if cmd == "add":
            cmd_set.add(num)
        elif cmd == "remove":
            cmd_set.discard(num) # discard() 는 remove() 와 다르게 값이 없으면 오류를 출력시키지 않음
        elif cmd == "check":
            print(1 if num in cmd_set else 0)
        elif cmd == "toggle":
            if num in cmd_set:
                cmd_set.discard(num)
            else:
                cmd_set.add(num)

