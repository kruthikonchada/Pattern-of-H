num = int(input())
spaces = num - 1
for i in range(1, num+1):
    print(' ' * spaces, end='')
    for j in range(1, i+1):
        print(num, end='')
        num = num + 1
    print()
    spaces = spaces - 1
    num = num - i - 1
