#/usr/bin/python

xPos = 0
yPos = 2
code = []

def main():
    path = open('input.txt').read().strip().split('\n')
    keypad = [['1','2','3'],['4','5','6'],['7','8','9']]
    for direction in path:
        for x in range(0,len(direction)):
            coord_move(direction[x], keypad)
            if x == (len(direction)-1):
                code.append(keypad[yPos][xPos])
    print(''.join(code))

def coord_move(direction, keypad):
    global xPos
    global yPos
    if direction == 'U':
        yPos-=1
        if is_out_of_bounds(yPos) == True:
            yPos+=1
    elif direction == 'R':
        xPos+=1
        if is_out_of_bounds(xPos) == True:
            xPos-=1
    elif direction == 'D':
        yPos+=1
        if is_out_of_bounds(yPos) == True:
            yPos-=1
    elif direction == 'L':
        xPos-=1
        if is_out_of_bounds(xPos) == True:
            xPos+=1

def is_out_of_bounds(pos):
    if pos > 2:
        return True
    elif pos < 0:
        return True
    else:
        return False

keypad2 = [['-1','-1','1','-1','-1'], ['-1','2','3','4','-1'],['5','6','7','8','9'],['-1','A','B','C','-1'],['-1','-1','D','-1','-1']]

def main2():
    path = open('input.txt').read().strip().split('\n')
    for direction in path:
        for x in range(0,len(direction)):
            coord_move2(direction[x], keypad2)
            if x == (len(direction)-1):
                code.append(keypad2[yPos][xPos])
    print(''.join(code))

def coord_move2(direction, keypad):
    global xPos
    global yPos
    if direction == 'U':
        yPos-=1
        if is_out_of_bounds2(yPos,xPos,yPos) == True:
            yPos+=1
    elif direction == 'R':
        xPos+=1
        if is_out_of_bounds2(yPos,xPos,xPos) == True:
            xPos-=1
    elif direction == 'D':
        yPos+=1
        if is_out_of_bounds2(yPos,xPos,yPos) == True:
            yPos-=1
    elif direction == 'L':
        xPos-=1
        if is_out_of_bounds2(yPos,xPos,xPos) == True:
            xPos+=1

def is_out_of_bounds2(yPos,xPos, pos):
    if pos > 4 or pos < 0:
        return True
    if keypad2[yPos][xPos] == '-1':
        return True
    return False

main()
code = []
main2()
