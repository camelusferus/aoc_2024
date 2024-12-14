push_options = [(a,b) for a in range(101) for b in range(101)]
push_options.sort(key=lambda x: 3*x[0]+x[1])

def worker(game):
    for push_option in push_options:
        if (push_option[0]*game['A'][0] + push_option[1]*game['B'][0] == game['Puzzle'][0] and
            push_option[0]*game['A'][1] + push_option[1]*game['B'][1] == game['Puzzle'][1]):
            return push_option[0]*3 + push_option[1]
    return 0

input = [{
    'A':(list(map(lambda x: float(x[2:]),group.split("\n")[0].split(": ")[1].split(", ")))),
    'B':(list(map(lambda x: float(x[2:]),group.split("\n")[1].split(": ")[1].split(", ")))),
    'Puzzle':(list(map(lambda x: float(x[2:]),group.split("\n")[2].split(": ")[1].split(", ")))),
} for group in open("input/input_13.txt").read().strip().split("\n\n")]

print(sum([worker(game) for game in input]))