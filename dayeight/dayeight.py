#/usr/bin/python

from collections import deque

def main():

    w, h = 50, 6
    screen = [[0 for x in range(w)] for y in range(h)]
    #print(screen)

    operations = open('input.txt').read().strip().split('\n')

    for operation in operations:
        operation_list = operation.split(' ')
        if operation_list[0] == "rect":
            xy = ''.join(operation_list[1]).split('x')
            y = int(xy[0])-1
            x = int(xy[1])-1
            screen[x][y] = '#'
        elif operation_list[0] == 'rotate':
            if operation_list[1] == 'row':
                rotate_count = int(operation_list[2].split('=')[1])
                for alist in screen:

            elif operation_list[1] == 'column':
                rotate_count = operation_list[2].split('=')[1]

    for shit in screen:
        print(shit)

def rotate(l, n):
    return l[n:] + l[:n]

main()
