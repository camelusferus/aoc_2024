input = [a for a in open("input/input_11.txt").read().strip().split(" ")]

for i in range(25):
    new_input = []
    for stone in input:
        if stone == '0':
            new_input.append('1')
        elif len(stone)%2 == 0:
            new_input.append(str(int(stone[:len(stone)//2])))
            new_input.append(str(int(stone[len(stone)//2:])))
        else:
            new_input.append(str(2024 * int(stone)))
    input = new_input

print(len(input))