input = [{
    'A':(list(map(lambda x: int(x[2:]),group.split("\n")[0].split(": ")[1].split(", ")))),
    'B':(list(map(lambda x: int(x[2:]),group.split("\n")[1].split(": ")[1].split(", ")))),
    'Puzzle':(list(map(lambda x: int(x[2:]) + 10000000000000,group.split("\n")[2].split(": ")[1].split(", ")))),
} for group in open("input/input_13.txt").read().strip().split("\n\n")]
tokens = 0

for game in input:
    # det <> 0: single solution
    if game['A'][0]*game['B'][1] - game['A'][1]*game['B'][0] != 0:
        # gaussian elimination
        if (game['A'][0]*game['Puzzle'][1]-game['A'][1]*game['Puzzle'][0]) % (game['A'][0]*game['B'][1] - game['A'][1]*game['B'][0]) > 0:
            continue
        B = (game['A'][0]*game['Puzzle'][1]-game['A'][1]*game['Puzzle'][0])/(game['A'][0]*game['B'][1] - game['A'][1]*game['B'][0])
        if (game['Puzzle'][0]-B*game['B'][0]) % game['A'][0] > 0:
            continue
        A = (game['Puzzle'][0]-B*game['B'][0]) / game['A'][0]
        if A < 0 or B < 0:
            continue
        tokens += 3*A + B
    else:
        if game['A'][0]*game['Puzzle'][1] - game['A'][1]*game['Puzzle'][0] == 0:
            continue
        if game['A'][0] > 3*game['B'][0]:
            A_temp = game['Puzzle'][0] // game['A'][0]
            B_temp = 0
            solved = False
            while True:
                if A_temp < 0:
                    break
                if A_temp * game['A'][0]  + B_temp + game['B'][0] == game['Puzzle'][0]:
                    solved = True
                    break
                if A_temp * game['A'][0]  + B_temp + game['B'][0] < game['Puzzle'][0]:
                    B_temp += 1
                    continue
                if A_temp * game['A'][0]  + B_temp + game['B'][0] > game['Puzzle'][0]:
                    A_temp -= 1
                    continue
            if solved:
                tokens += 3*A + B

print(tokens)