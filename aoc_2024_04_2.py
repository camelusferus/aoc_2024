field = [[char for char in line]  + [" "] for line in open("input/input_04.txt").read().strip().split("\n")]
field.append([" " for a in field[0]])
adjacencies = [[1,1],[1,-1],[-1,-1],[-1,1]]
print(sum([sum([sum([1 for a in range(len(adjacencies)) if 'A' == field[i][j] and
                    'M' == field[i+adjacencies[a][0]][j+adjacencies[a][1]] and
                    'M' == field[i+adjacencies[(a+1)%4][0]][j+adjacencies[(a+1)%4][1]] and
                    'S' == field[i+adjacencies[(a+2)%4][0]][j+adjacencies[(a+2)%4][1]] and
                    'S' == field[i+adjacencies[(a+3)%4][0]][j+adjacencies[(a+3)%4][1]]]) for j in range(len(field[i]))]) for i in range(len(field))]))