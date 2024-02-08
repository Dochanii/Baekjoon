import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    order = sys.stdin.readline().split()
    if 'push' == order[0]:
        stack.append(int(order[1]))
    elif 'top' == order[0]:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif 'pop' == order[0]:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' == order[0]:
        print(len(stack))
    else:
        if stack:
            print(0)
        else:
            print(1)