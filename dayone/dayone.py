#!/usr/bin/python
path = open('input.txt').read().strip().split(', ')

def main():
    compass = 'north'
    y = 0
    x = 0
    all_cords = []
    for direction_and_steps in path:
        tempvar = direction_and_steps
        direction = tempvar[0]
        steps = int(tempvar[1:])

        if compass == 'north':
            if direction == 'L':
                compass = 'west'
            else:
                compass = 'east'
        elif compass == 'east':
            if direction == 'L':
                compass = 'north'
            else:
                compass = 'south'
        elif compass == 'south':
            if direction == 'L':
                compass = 'east'
            else:
                compass = 'west'
        else:
            if direction == 'L':
                compass = 'south'
            else:
                compass = 'north'

        if compass == 'north':
            y+=steps
        elif compass == 'east':
            x+=steps
        elif compass == 'south':
            y-=steps
        else:
            x-=steps
        print('X: ',x,' Y: ',y,' Compass: ',compass)
        cord_str = str(x)+'-'+str(y)
        if cord_str in all_cords:
            print(cord_str)
        all_cords.append(cord_str)


    blocks = abs(x) + abs(y)
    print(blocks)

main()
