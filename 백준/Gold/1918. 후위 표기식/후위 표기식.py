import sys

op_expressions = sys.stdin.readline().rstrip()
ans = ""
stack = []
for i in op_expressions:
    if i.isalpha():
        ans += i
    elif i == '(':
        stack.append(i)
    elif i == '*' or i =='/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans+=stack.pop()
        stack.append(i)
        
    elif i == '+' or i =='-':
        while stack and stack[-1] != '(':
            ans+=stack.pop()
        stack.append(i)
    else:
        while stack and stack[-1] !='(':
            ans += stack.pop()
        stack.pop()
while stack:
    ans += stack.pop()
    
print(ans)
                