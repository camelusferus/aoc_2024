f = open("input/input_15.txt").read().strip().split("\n\n")
doubling = lambda x: '##' if x == '#' else ('..' if x == '.' else ('[]' if x == 'O' else '@.'))
field = [[x for a in line for x in doubling(a)] for line in f[0].split("\n")]
actions = [a for a in f[1] if a in ['<','v','>','^']]
position = [(x[0],y[0]) for y in enumerate(field) for x in enumerate(y[1]) if field[y[0]][x[0]] == '@'][0]

def walk_check(position,direction):
    next_x, next_y = -1,-1
    match direction:
        case '^':
            next_x, next_y = position[0],position[1]-1
        case 'v':
            next_x, next_y = position[0],position[1]+1
    if field[next_y][next_x] == '#':
        return False
    if field[next_y][next_x] == '.':
        return True
    if field[next_y][next_x] == '[':
        return walk_check((next_x,next_y),direction) and walk_check((next_x + 1,next_y),direction)
    if field[next_y][next_x] == ']':
        return walk_check((next_x - 1,next_y),direction) and walk_check((next_x,next_y),direction)

def walk_new(position, direction):
    next_x, next_y = -1,-1
    current_holder = field[position[1]][position[0]]
    match direction:
        case '^':
            next_x, next_y = position[0],position[1]-1
        case 'v':
            next_x, next_y = position[0],position[1]+1
    if field[next_y][next_x] == '.':
        field[next_y][next_x] = current_holder
        field[position[1]][position[0]] = '.'
        return
    elif field[next_y][next_x] == '[':
        walk_new((next_x, next_y), direction)
        walk_new((next_x + 1, next_y), direction)
        field[next_y][next_x] = current_holder
        field[position[1]][position[0]] = '.'
        return
    elif field[next_y][next_x] == ']':
        walk_new((next_x - 1, next_y), direction)
        walk_new((next_x, next_y), direction)
        field[next_y][next_x] = current_holder
        field[position[1]][position[0]] = '.'
        return



# TODO: 2 phase walk
def walk_orig(position, direction):
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
    if field[next_y][next_x] in ['[',']']:
        if walk_orig((next_x, next_y), direction) == (-1, -1):
            return (-1,-1)
        else:
            field[next_y][next_x] = current_holder
            field[position[1]][position[0]] = '.'
            return (next_x, next_y)

for action in actions:
    walk_result = (-1,-1)
    if action in ['^','v']:
        if walk_check(position,action):
            walk_new(position,action)
            if action == '^':
                walk_result = (position[0],position[1]-1)
            else:
                walk_result = (position[0],position[1]+1)
    elif action in ['<','>']:
        walk_result = walk_orig(position, action)

    if walk_result != (-1,-1):
        position = walk_result

print(sum([100 * y[0] + x[0] for y in enumerate(field) for x in enumerate(y[1]) if x[1] in ['[',]]))