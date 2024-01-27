write_num = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
strings = input()
res = 0
for i in range(len(strings)):
    res += write_num[ord(strings[i])-65]
    if(res>10):
        res = res%10
if(res%2):
    print("I'm a winner!")
else:
    print("You're the winner?")