input = open("input/input_01.txt").read().replace("   ", "\n").strip().split("\n")
left = list(map(int, input[0::2]))
right = list(map(int, input[1::2]))
left.sort()
right.sort()
print(sum([abs(i - j) for (i, j) in zip(left, right)]))
