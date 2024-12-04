field = [[char for char in line]  + [" "] for line in open("input/input_04.txt").read().strip().split("\n")]
field.append([" " for a in field[0]])
print(sum([sum([sum([1 for directions in [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)] if
                    'X' == field[i][j] and
                    'M' == field[i+directions[0]][j+directions[1]] and
                    'A' == field[i+directions[0]*2][j+directions[1]*2] and
                    'S' == field[i+directions[0]*3][j+directions[1]*3]]) for j in range(len(field[i]))]) for i in range(len(field))]))