f = open("input/input_15.txt").read().strip().split("\n\n")
field = [[a for a in line] for line in f[0].split("\n")]
actions = [a for a in f[1] if a in ['<','v','>','^']]
position = [(x[0],y[0]) for y in enumerate(field) for x in enumerate(y[1]) if field[x[0]][y[0]] == '@'][0]

def walk(position,direction):
    next_x, next_y = -1,-1
    current_holder = field[position[1]][position[0]]
    match direction:
        case '<':
            next_x, next_y = position[0]-1,position[1]
        case '^':
            next_x, next_y = position[0],position[1]-1
        case '>':
            next_x, next_y = position[0]+1,position[1]
        case 'v':
            next_x, next_y = position[0],position[1]+1
    if field[next_y][next_x] == '#':
        return (-1,-1)
    if field[next_y][next_x] == '.':
        field[next_y][next_x] = current_holder
        field[position[1]][position[0]] = '.'
        return (next_x,next_y)
    if field[next_y][next_x] == 'O':
        if walk((next_x,next_y),direction) == (-1,-1):
            return (-1,-1)
        else:
            field[next_y][next_x] = current_holder
            field[position[1]][position[0]] = '.'
            return (next_x, next_y)

for action in actions:
    walk_result = walk(position,action)
    if walk_result != (-1,-1):
        position = walk_result

print(sum([100 * y[0] + x[0] for y in enumerate(field) for x in enumerate(y[1]) if x[1] == 'O']))