from multiprocessing import Pool

def base3(x):
    result = ""
    while x:
        x,r = divmod(x,3)
        result = str(r)+result
    return result

def worker(i):
    for j in range(3 ** (len(i['values'])), 3 * 3 ** len(i['values'])):
        calcuation = i['values'][0]
        for k in enumerate(i['values']):
            if k[0] == 0:
                continue
            if (base3(j)[k[0] + 1] == '0'):
                calcuation += int(k[1])
            elif (base3(j)[k[0] + 1] == '1'):
                calcuation *= int(k[1])
            elif (base3(j)[k[0] + 1] == '2'):
                calcuation = int(str(calcuation) + str(k[1]))
        if int(calcuation) == i['result']:
            return i['result']
    return 0

input = [ {'result': int(line.split(":")[0]), 'values': list(map(int,line.split(":")[1].strip().split()))} for line in open("input/input_07.txt").read().strip().split("\n")]
pool = Pool()
results = pool.map(worker, input)
print(results)
print(sum(results))