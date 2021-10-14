import sys

n = int(input())
stack = []
for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd[:4] == 'push':
        push, num = cmd.split()
        stack.append(int(num))
    elif cmd == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(1 if not stack else 0)
    elif cmd == 'top':
        print(-1 if not stack else stack[-1])