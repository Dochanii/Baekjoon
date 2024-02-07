import sys

def is_palindrome(temp_lst):
    standard = len(temp_lst)//2
    if len(temp_lst)%2:
        if temp_lst[:standard] == temp_lst[len(temp_lst)-1:standard:-1]:
            return 1  
    else:
        if temp_lst[:standard] == temp_lst[len(temp_lst)-1:standard-1:-1]:
            return 1
    return 0
    
n = int(sys.stdin.readline())
tmp_word = ''
tmp_word2 = ''

for _ in range(n):
    strings = input()
    first = 0
    end = len(strings)-1
    flag = False
    if is_palindrome(strings):
        flag = True
        print(0)
    else:
        while first<end:
            if strings[first] == strings[end]:
                first += 1
                end -=1
            else:
                tmp_word = strings[:first] + strings[first+1:]
                tmp_word2 = strings[:end]+strings[end+1:]
                if is_palindrome(tmp_word) or is_palindrome(tmp_word2):
                    flag = True
                    print(1)
                    break
                else:
                    print(2)
                    break
        
