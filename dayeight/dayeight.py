#/usr/bin/python

from collections import deque

def main():

    screen = deque([['.'] * 50, ['.'] * 6])
    print(screen)

    operations = open('input.txt').read().strip().split('\n')

    for operation in operations:
        operation_list = operation.split(' ')
        if operation_list[0] == "rect":
            xy = ''.join(operation_list[1]).split('x')
            x = int(xy[0])-1
            y = int(xy[1])-1
            screen[x][y] = '#'
        elif operation_list[0] == 'rotate':
            if operation_list[1] == 'row':
                pass
            elif operation_list[1] == 'column':
                pass
    print(screen)

main()
