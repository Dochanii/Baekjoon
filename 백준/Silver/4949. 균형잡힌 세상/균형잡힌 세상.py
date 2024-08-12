import sys
input = sys.stdin.readline

stack = []
no_condition = False


while True:
    input_string = input().rstrip()
    stack.clear()
    no_condition = False
    if(input_string == "."):
        break
    for i in input_string:
        if i == '(':
            stack.append(i)
            
        elif i == ')':
            if stack:
                if stack[-1] == '[':
                    no_condition = True
                    break
                else:
                    stack.pop()
            else:
                no_condition = True
                break
                
        elif i == '[':
            stack.append(i)
            
        elif i == ']':
            if stack:
                if stack[-1] == '(':
                    no_condition = True
                    break
                else:
                    stack.pop()
            else:
                no_condition = True
                break
    
    if not stack and input_string[-1] == '.' and not no_condition:
        print("yes")
    else:
        print("no")
        
    