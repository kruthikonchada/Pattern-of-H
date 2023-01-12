a = int(input("Enter an odd number:"))
count = a
max = 0
if a%2 != 0:
    spaces = a * 3
    b = int(a / 2)
    c = a - 1
    even = int(c / 2)
    width = a * 5
    str = ''
    for i in range(a):
        if i == 0:
            str = str + 'H'
            print(str.rjust(count), '')
            max = max + 1
        else:
            for j in range(2):
                str = str + 'H'
                max = max + 1
            count += 1
            print(str.rjust(count), '')
    str = ''
    for i in range(a + 1):
        for j in range(spaces):
            str = str + ' '
        str = str.center(width, 'H')
        str = str.rjust(width + b, ' ')
        print(str.ljust(width+b+1, ' '))
        str = ''
    for j in range(a):
        for i in range(width):
            str = str + 'H'
        str = str.rjust(width+b, ' ')
        print(str.ljust(width+b+1, ' '))
        str = ''
    for i in range(a + 1):
        for j in range(spaces):
            str = str + ' '
        str = str.center(width, 'H')
        str = str.rjust(width + b, ' ')
        print(str.ljust(width+b+1, ' '))
        str = ''
    for i in range(a):
        for j in range(a + c):
            str = str + 'H'
        c = c - 2
        str = str.center(max, ' ')
        str = str.rjust(width+b+even, ' ')
        str = str + ' '
        print(str)
        str = ''
else:
    print("It should be an even number.")