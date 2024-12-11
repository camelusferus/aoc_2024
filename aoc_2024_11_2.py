input = open("input/input_11.txt").read().strip().split(" ")
input_values = {int(i):input.count(i) for i in input}

for blinking in range(75):
    new_values = {}
    for key,count in input_values.items():
        if key == 0:
            new_values[1] = count if 1 not in new_values else new_values[1] + count
        elif len(str(key))%2 == 0:
            new_values[int(str(key)[:len(str(key))//2])] = count if int(str(key)[:len(str(key))//2]) not in new_values else new_values[int(str(key)[:len(str(key))//2])] + count
            new_values[int(str(key)[len(str(key))//2:])] = count if int(str(key)[len(str(key))//2:]) not in new_values else new_values[int(str(key)[len(str(key))//2:])] + count
        else:
            new_values[key*2024] = count if key*2024 not in new_values else new_values[key*2024] + count
    input_values = new_values

print(sum([count for key,count in new_values.items()]))