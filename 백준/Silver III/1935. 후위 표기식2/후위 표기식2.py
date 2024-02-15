import sys
n = int(sys.stdin.readline())
input_string = sys.stdin.readline().rstrip()
stack = []
num_lst=[]
for i in range(n):
    num_lst.append(int(sys.stdin.readline()))

for i in input_string:
    
    if i.isalpha():
        stack.append(num_lst[ord(i)-ord('A')])
    else:
        oper_num1 = stack.pop()
        oper_num2 = stack.pop()
        if i == '+':
            stack.append(oper_num2+oper_num1)
        elif i == '-':
            stack.append(oper_num2-oper_num1)
        elif i == '*':
            stack.append(oper_num2*oper_num1)
        elif i == '/':
            stack.append(oper_num2/oper_num1)
print("%.2f" %stack[0])