reports = [list(map(int,line.split(" "))) for line in open("input/input_02.txt").read().strip().split("\n")]
print(sum([1 for report in reports if any([True
             for alternate_report in [report[:a] + report[a+1:] for a in range(len(report)+1)] if
                set(dict.fromkeys([int(alternate_report[i]) - int(alternate_report[i+1]) for i in range(len(alternate_report) - 1)])).issubset([1,2,3]) or
                set(dict.fromkeys([int(alternate_report[i]) - int(alternate_report[i+1]) for i in range(len(alternate_report) - 1)])).issubset([-1,-2,-3])])]))