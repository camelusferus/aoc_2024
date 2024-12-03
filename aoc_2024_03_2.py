import re
relevant = open("input/input_03.txt").read().split("don't()")[0] + ''.join([''.join(piece.split('do()')[1:]) for piece in open("input/input_03.txt").read().split("don't()")[1:]])
print(sum([int(a[0])*int(a[1]) for a in map(lambda x: x[4:-1].split(","), re.findall(r'mul\(\d+,\d+\)',relevant))]))