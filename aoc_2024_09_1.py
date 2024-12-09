input = [a[0]//2 if not a[0]%2 else -1 for a in enumerate(open("input/input_09.txt").read().strip()) for b in range(int(a[1]))]
input_rev = input[::-1]
for i in range(input.count(-1)-2):
    first_free = input.index(-1)
    print(first_free)
    last_free = len(input) - 1 - list(filter(lambda x: x[1]!=-1, enumerate(input[::-1])))[0][0]
    if first_free > last_free:
        break
    input[first_free], input[last_free] = input[last_free], input[first_free]
input2 = input[:input.index(-1)]
print(sum([i[0]*i[1] for i in enumerate(input2)]))