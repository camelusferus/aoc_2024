import copy

input = [(int(a[1]),a[0]//2,a[0]) if not a[0]%2 else (int(a[1]),-1,a[0]) for a in enumerate(open("input/input_09.txt").read().strip()) ]
for j in range(input[-1][1],-1,-1):
    location = -1
    for i in enumerate(input):
        if i[1][1] == j:
            temp = copy.deepcopy(i[1])
            location = i[0]
            break
    if location == -1:
        continue
    for i in enumerate(input[:location]):
        if i[1][1] == -1 and i[1][0] >= temp[0]:
            input[location] = (temp[0],-1,-1)
            if i[1][0] == temp[0]:
                replacement = [temp,]
            else:
                replacement = [temp,(i[1][0]-temp[0],-1,i[1][2])]
            input = input[:i[0]] + replacement + input[i[0]+1:]
            new_empty_index = input.index((temp[0],-1,-1))
            new_empty_element = input[input.index((temp[0],-1,-1))]
            if new_empty_index + 1 < len(input) and input[new_empty_index+1][1] == -1:
                replacement = (new_empty_element[0] + input[new_empty_index+1][0], new_empty_element[1], new_empty_element[2])
                input[new_empty_index] = replacement
                del input[new_empty_index+1]
                new_empty_index = input.index(replacement)
                new_empty_element = input[input.index(replacement)]
            if input[new_empty_index-1][1] == -1:
                input[new_empty_index] = (new_empty_element[0] + input[new_empty_index-1][0], new_empty_element[1], new_empty_element[2])
                del input[new_empty_index-1]
            break
sum = 0
mult = 0
for i in input:
    if i[1] == -1:
        mult += i[0]
        continue
    for a in range(i[0]):
        sum += i[1]*mult
        mult += 1

print(sum)
