import sys

field = [[a for a in line ]for line in open("input/input_16.txt").read().strip().split("\n")]
max_cost_field = [[{0: 10**20} for a in range(len(field[0]))] for b in range(len(field))]
best_paths_field = [['' for a in range(len(field[0]))] for b in range(len(field))]
position = [(x[0],y[0]) for y in enumerate(field) for x in enumerate(y[1]) if field[y[0]][x[0]] == 'S'][0]
current_direction = 0 # 0 - right, 1 - down, 2 - left, 3 - up
best_solution = 10**20

sys.setrecursionlimit(10000)

def explore(x,y,current_cost,direction,path,count_solutions):
    global best_solution
    best_path = False
    if field[y][x] == 'E':
        if (current_cost <= best_solution):
            best_solution = current_cost
            best_paths_field[y][x] = 'O'
            return True
    else:
        if best_solution < current_cost:
            return False
        if direction in max_cost_field[y][x].keys():
            if max_cost_field[y][x][direction] < current_cost:
                return False
        max_cost_field[y][x][direction] = current_cost
        if min(max_cost_field[y][x].get(i,10**20) for i in range(4)) + 1000 < current_cost:
            return False
        match direction:
            case 0:
                if field[y][x+1] != '#' and (x+1,y) not in path:
                    best_path = explore(x+1,y,current_cost+1,0,path+[(x,y)],count_solutions) or best_path
                if field[y+1][x] != '#' and (x,y+1) not in path:
                    best_path = explore(x,y+1,current_cost+1001,1,path + [(x,y)],count_solutions) or best_path
                if field[y-1][x] != '#' and (x,y-1) not in path:
                    best_path = explore(x,y-1,current_cost+1001,3,path + [(x,y)],count_solutions) or best_path
            case 1:
                if field[y+1][x] != '#' and (x,y+1) not in path:
                    best_path = explore(x,y+1,current_cost+1,1,path + [(x,y)],count_solutions) or best_path
                if field[y][x-1] != '#' and (x-1,y) not in path:
                    best_path = explore(x-1,y,current_cost+1001,2,path + [(x,y)],count_solutions) or best_path
                if field[y][x+1] != '#' and (x+1,y) not in path:
                    best_path = explore(x+1,y,current_cost+1001,0,path + [(x,y)],count_solutions) or best_path
            case 2:
                if field[y][x-1] != '#' and (x-1,y) not in path:
                    best_path = explore(x-1,y,current_cost+1,2,path + [(x,y)],count_solutions) or best_path
                if field[y+1][x] != '#' and (x,y+1) not in path:
                    best_path = explore(x,y+1,current_cost+1001,1,path + [(x,y)],count_solutions) or best_path
                if field[y-1][x] != '#' and (x,y-1) not in path:
                    best_path = explore(x,y-1,current_cost+1001,3,path + [(x,y)],count_solutions) or best_path
            case 3:
                if field[y-1][x] != '#' and (x,y-1) not in path:
                    best_path = explore(x,y-1,current_cost+1,3,path + [(x,y)],count_solutions) or best_path
                if field[y][x-1] != '#' and (x-1,y) not in path:
                    best_path = explore(x-1,y,current_cost+1001,2,path + [(x,y)],count_solutions) or best_path
                if field[y][x+1] != '#' and (x+1,y) not in path:
                    best_path = explore(x+1,y,current_cost+1001,0,path + [(x,y)],count_solutions) or best_path
        if count_solutions and best_path:
            best_paths_field[y][x] = 'O'
        return best_path

explore(position[0],position[1],0,0,[],False)
explore(position[0],position[1],0,0,[],True)
print(len(''.join([''.join(a) for a in best_paths_field])))