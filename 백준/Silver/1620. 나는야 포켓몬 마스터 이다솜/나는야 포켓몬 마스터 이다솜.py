import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())

poketmon_dict = defaultdict(str)
reversed_poketmon_dict = defaultdict(int)

for i in range(1,n+1):
    poketmon = sys.stdin.readline().rstrip()
    poketmon_dict[i]=poketmon
    reversed_poketmon_dict[poketmon]=i

for j in range(m):
    quiz = sys.stdin.readline().rstrip()
    if quiz.isdigit():
        print(poketmon_dict[int(quiz)])
    else:
        print(reversed_poketmon_dict[quiz])
        
    
