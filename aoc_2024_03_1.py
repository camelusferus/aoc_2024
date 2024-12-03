import re
print(sum([int(a[0])*int(a[1]) for a in map(lambda x: x[4:-1].split(","), re.findall(r'mul\(\d+,\d+\)',open("input/input_03.txt").read()))]))