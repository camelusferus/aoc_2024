hits = [tuple(map(int,a.split(','))) for a in open("input/input_18.txt").read().strip().split("\n")]

def path_tester(iterations):
    field = [[0 for a in range(71+2)] for b in range(71+2)]
    for i in range(len(field)):
        field[0][i],field[i][0],field[len(field)-1][i],field[i][len(field)-1] = 1,1,1,1
    for i in range(iterations):
        field[hits[i][1]+1][hits[i][0]+1] = 1
    visit_queue = [(0,(1,1))]

    while len(visit_queue):
        exploration = visit_queue.pop(0)
        if (exploration[1][0], exploration[1][1]) == (70+1, 70+1):
            return exploration[0]
        if not field[exploration[1][1]-1][exploration[1][0]]:
            field[exploration[1][1]-1][exploration[1][0]] = 4
            visit_queue.append((exploration[0]+1,(exploration[1][0],exploration[1][1]-1)))
        if not field[exploration[1][1]+1][exploration[1][0]]:
            field[exploration[1][1]+1][exploration[1][0]] = 4
            visit_queue.append((exploration[0]+1,(exploration[1][0],exploration[1][1]+1)))
        if not field[exploration[1][1]][exploration[1][0]-1]:
            field[exploration[1][1]][exploration[1][0]-1] = 4
            visit_queue.append((exploration[0]+1,(exploration[1][0]-1,exploration[1][1])))
        if not field[exploration[1][1]][exploration[1][0]+1]:
            field[exploration[1][1]][exploration[1][0]+1] = 4
            visit_queue.append((exploration[0]+1,(exploration[1][0]+1,exploration[1][1])))
    return -1

path_lengths = list(map(path_tester,range(len(hits))))
print(hits[path_lengths.index(-1)-1])
