import copy

direction_order = ['^', '<', 'v', '>']

def probe(input,guard,direction):
    i = 4 * len(input)*len(input[0])
    while i>0:
        match direction:
            case ">":
                new_guard = (guard[0]+1,guard[1])
            case "^":
                new_guard = (guard[0],guard[1]-1)
            case "<":
                new_guard = (guard[0]-1,guard[1])
            case "v":
                new_guard = (guard[0],guard[1]+1)
     #   print(new_guard)
        if (input[new_guard[1]][new_guard[0]] in ['#','O']):
            direction = direction_order[direction_order.index(direction)-1]
            i -= 1
            continue
        input[guard[1]][guard[0]] = 'X'
        guard = new_guard
        if ((new_guard[0] <= 0 and direction == '<') or (new_guard[0] >= len(input[0]) - 1 and direction == '>') or (new_guard[1] <= 0 and direction == '^') or (new_guard[1] >= len(input) - 1 and direction == 'v')):
            input[guard[1]][guard[0]] = 'X'
            return 0
        # print('\n'.join([''.join(field) for field in input]))
        # print()
        i -= 1
    #     print()
    #print('\n\n\n')
    return 1

input = [[char for char in line] for line in open("input/input_06.txt").read().strip().split("\n")]
guard = [([field[0] for field in enumerate(line[1]) if field[1] in direction_order][0],line[0]) for line in enumerate(input) if len([field[0] for field in enumerate(line[1]) if field[1] in direction_order])==1 ][0]
direction = input[guard[1]][guard[0]]
input[guard[1]][guard[0]] = "X"
stuck = 0
for i in range(len(input[1])):
    for j in range(len(input)):
        match direction:
            case ">":
                new_guard = (guard[0]+1,guard[1])
            case "^":
                new_guard = (guard[0],guard[1]-1)
            case "<":
                new_guard = (guard[0]-1,guard[1])
            case "v":
                new_guard = (guard[0],guard[1]+1)
        if ((i,j) == new_guard or input[j][i] == '#'):
            continue
        test_direction = copy.deepcopy(direction) #direction_order[direction_order.index(direction)-1]
        test_input = copy.deepcopy(input)
        test_input[j][i] = 'O'
        stuck += probe(test_input,copy.deepcopy(guard),test_direction)
print(stuck)
