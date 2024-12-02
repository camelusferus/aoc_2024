reports = [line.split(" ") for line in open("input/input_02.txt").read().strip().split("\n")]
intervals = [set(dict.fromkeys([int(report[i]) - int(report[i+1]) for i in range(len(report) - 1)])) for report in reports]
print(sum([1 for interval in intervals if interval.issubset([1,2,3]) or interval.issubset([-1,-2,-3])]))