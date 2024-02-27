import sys
n = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
B = [int(x) for x in sys.stdin.readline().rstrip().split()]


for i in B:
    if i in A:
        print(1)
    else:
        print(0)
        

    
