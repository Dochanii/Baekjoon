import sys
n = int(sys.stdin.readline().rstrip())


for i in range (n):
    stack = []
    p = input()
    for j in p:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
