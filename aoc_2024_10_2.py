input = [[int(a)  if a != '.' else '.' for a in line] for line in open("input/input_10.txt").read().strip().split("\n")]
sum_single = 0
adjacencies = [[-1,0],[0,-1],[0,1],[1,0]]
for i in range(len(input[0])):
    for j in range(len(input)):
        if input[j][i] == 0:
            null = [i,j]
            for adj1 in adjacencies:
                one = list(map(sum,zip(null,adj1)))
                if not 0 <= one[0] < len(input[0]) or not 0 <= one[1] < len(input):
                    continue
                if input[one[1]][one[0]] != 1:
                    continue
                for adj2 in adjacencies:
                    two = list(map(sum,zip(one,adj2)))
                    if (not 0 <= two[0] < len(input[0])) or (not 0 <= two[1] < len(input)):
                        continue
                    if input[two[1]][two[0]] != 2:
                        continue
                    for adj3 in adjacencies:
                        three = list(map(sum,zip(two,adj3)))
                        if not 0 <= three[0] < len(input[0]) or not 0 <= three[1] < len(input):
                            continue
                        if input[three[1]][three[0]] != 3:
                            continue
                        for adj4 in adjacencies:
                            four = list(map(sum,zip(three,adj4)))
                            if not 0 <= four[0] < len(input[0]) or not 0 <= four[1] < len(input):
                                continue
                            if input[four[1]][four[0]] != 4:
                                continue
                            for adj5 in adjacencies:
                                five = list(map(sum,zip(four,adj5)))
                                if not 0 <= five[0] < len(input[0]) or not 0 <= five[1] < len(input):
                                    continue
                                if input[five[1]][five[0]] != 5:
                                    continue
                                for adj6 in adjacencies:
                                    six = list(map(sum,zip(five,adj6)))
                                    if not 0 <= six[0] < len(input[0]) or not 0 <= six[1] < len(input):
                                        continue
                                    if input[six[1]][six[0]] != 6:
                                        continue
                                    for adj7 in adjacencies:
                                        seven = list(map(sum,zip(six,adj7)))
                                        if not 0 <= seven[0] < len(input[0]) or not 0 <= seven[1] < len(input):
                                            continue
                                        if input[seven[1]][seven[0]] != 7:
                                            continue
                                        for adj8 in adjacencies:
                                            eight = list(map(sum,zip(seven,adj8)))
                                            if not 0 <= eight[0] < len(input[0]) or not 0 <= eight[1] < len(input):
                                                continue
                                            if input[eight[1]][eight[0]] != 8:
                                                continue
                                            for adj9 in adjacencies:
                                                nine = list(map(sum,zip(eight,adj9)))
                                                if not 0 <= nine[0] < len(input[0]) or not 0 <= nine[1] < len(input):
                                                    continue
                                                if input[nine[1]][nine[0]] != 9:
                                                    continue
                                                sum_single += 1
print(sum_single)