import sys
k = int(sys.stdin.readline())
stack = []
for i in range(k):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
res = 0
for i in stack:
    res +=i
print(res)