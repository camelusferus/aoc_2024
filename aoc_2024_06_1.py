input = [[char for char in line] for line in open("input/input_06.txt").read().strip().split("\n")]
guard = [([field[0] for field in enumerate(line[1]) if field[1] in ["^","<","v",">"]][0],line[0]) for line in enumerate(input) if len([field[0] for field in enumerate(line[1]) if field[1] in ["^","<","v",">"]])==1 ][0]
direction = input[guard[1]][guard[0]]
input[guard[1]][guard[0]] = "X"
direction_order = ['^', '<', 'v', '>']
while True:
    match direction:
        case ">":
            new_guard = (guard[0]+1,guard[1])
        case "^":
            new_guard = (guard[0],guard[1]-1)
        case "<":
            new_guard = (guard[0]-1,guard[1])
        case "v":
            new_guard = (guard[0],guard[1]+1)
    if (input[new_guard[1]][new_guard[0]] == '#'):
        direction = direction_order[direction_order.index(direction)-1]
        continue
    input[guard[1]][guard[0]] = 'X'
    guard = new_guard
    if ((new_guard[0] <= 0 and direction == '<') or (new_guard[0] >= len(input[0]) - 1 and direction == '>') or (new_guard[1] <= 0 and direction == '^') or (new_guard[1] >= len(input) - 1 and direction == 'v')):
        input[guard[1]][guard[0]] = 'X'
        break
print(sum([sum([1 for field in line if field == "X"]) for line in input]))

