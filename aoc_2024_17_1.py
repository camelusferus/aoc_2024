input_file = open("input/input_17.txt").read().strip().split("\n")
a = int(input_file[0].split(": ")[1])
b = int(input_file[1].split(": ")[1])
c = int(input_file[2].split(": ")[1])
program = list(map(int,input_file[4].split(": ")[1].split(',')))
inst_pointer = 0
output = ''

while inst_pointer < len(program):
    operand = program[inst_pointer+1]
    combo_operand = 7
    match operand:
        case 0:
            combo_operand = 0
        case 1:
            combo_operand = 1
        case 2:
            combo_operand = 2
        case 3:
            combo_operand = 3
        case 4:
            combo_operand = a
        case 5:
            combo_operand = b
        case 6:
            combo_operand = c
    match program[inst_pointer]:
        case 0:
            a = a // (2**combo_operand)
        case 1:
            b = b ^ combo_operand
        case 2:
            b = combo_operand % 8
        case 3:
            if a != 0:
                if inst_pointer != combo_operand:
                    inst_pointer = combo_operand
                    continue
        case 4:
            b = b ^ c
        case 5:
            output += "{},".format(combo_operand % 8)
        case 6:
            b = a // (2**combo_operand)
        case 7:
            c = a // (2**combo_operand)
    inst_pointer += 2

print(output.rstrip(","))