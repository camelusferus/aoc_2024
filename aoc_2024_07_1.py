input = [ {'result': int(line.split(":")[0]), 'values': list(map(int,line.split(":")[1].strip().split()))} for line in open("input/input_07.txt").read().strip().split("\n")]
correct = 0
result = 0
for i in input:
    calcuation_possible = False
    for j in range(2**len(i['values']),2*2**len(i['values'])):
        calcuation = 0
        for k in enumerate(i['values']):
            if (bin(j)[2:][-k[0]-1] == '0'):
                calcuation += k[1]
            else:
                calcuation *= k[1]
        if calcuation == i['result']:
            calcuation_possible = True
            break
    if calcuation_possible:
        correct +=1
        result += i['result']
print(result)