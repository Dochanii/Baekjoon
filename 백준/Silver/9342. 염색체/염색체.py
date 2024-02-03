import sys
n = int(sys.stdin.readline())
test = 'AFC'
test_last_word = 'ABCDEF'
for i in range(n):
    XY = ''
    input_string = input()
    XY = ''.join(list(dict.fromkeys(input_string)))
    if test in XY and XY[-1] in test_last_word:
        print("Infected!")
    else:
        print("Good")