#/usr/bin/python

def main():

    w, h = 50, 6
    screen = [['.' for x in range(w)] for y in range(h)]
    #print(screen)

    operations = open('input.txt').read().strip().split('\n')

    for operation in operations:
        operation_list = operation.split(' ')
        if operation_list[0] == "rect":
            xy = ''.join(operation_list[1]).split('x')
            x = int(xy[0])
            y = int(xy[1])
            for x_pos in range(0,x):
                for y_pos in range(0,y):
                    screen[y_pos][x_pos] = '#'
        elif operation_list[0] == 'rotate':
            if operation_list[1] == 'row':
                rotate_position = int(operation_list[2].split('=')[1])
                rotate_count = int(operation_list[len(operation_list)-1])
                screen[rotate_position] = rotate(screen[rotate_position], rotate_count)
                print(screen)
                print('\n')
                print('\n')
            elif operation_list[1] == 'column':
                rotate_position = int(operation_list[2].split('=')[1])
                rotate_count = int(operation_list[len(operation_list)-1])
                column_list = []
                for x in range(0, 6):
                    column_list.append(screen[x][rotate_position])
                column_list = rotate(column_list, rotate_count)
                for x in range(0,6):
                    screen[x][rotate_position] = column_list[x]
                #screen[x] = rotate(screen[x], rotate_count)
                print(screen)
                print('\n')
                print('\n')

    print(screen)
    count = 0
    for x in screen:
        for y in x:
            if y == '#':
                count+=1
    print(count)

def rotate(l, n):
    return l[-n:] + l[:-n]

main()
