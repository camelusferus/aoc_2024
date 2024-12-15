from multiprocessing import Pool

field = [{'px': int(i.split(" ")[0][2:].split(",")[0]), 'py': int(i.split(" ")[0][2:].split(",")[1]),
          'vx': int(i.split(" ")[1][2:].split(",")[0]), 'vy': int(i.split(" ")[1][2:].split(",")[1])} for i in open("input/input_14.txt").read().strip().split("\n")]
field_x,field_y = 101,103
results = []

def worker(seconds):
    field_after_turn = [[(j['px'] + seconds * j['vx']) % field_x, (j['py'] + seconds * j['vy']) % field_y] for j in field]
    # one hopefully enough long piece of assembled robots
    if '################' in '\n'.join([''.join(['#' if len(list(filter(lambda x: x[0] == k and x[1] == j, field_after_turn))) > 0 else '.' for k in range(field_x)]) for j in range(field_y)]):
        print(str(seconds))
        return -1
    else:
        return -1

pool = Pool()
results = pool.map(worker,range(1,10000))
