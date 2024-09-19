import sys
input = sys.stdin.readline

n = int(input())
num_card = [0]*10

for i in str(n):
    if i=='6' or i =='9':
        if num_card[6] == num_card[9]:
            num_card[6] += 1
        else:
            num_card[9] += 1 
        
    else:
        num_card[int(i)] += 1
print(max(num_card))
