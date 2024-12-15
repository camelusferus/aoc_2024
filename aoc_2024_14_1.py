input = [{'px': int(i.split(" ")[0][2:].split(",")[0]), 'py': int(i.split(" ")[0][2:].split(",")[1]),
          'vx': int(i.split(" ")[1][2:].split(",")[0]), 'vy': int(i.split(" ")[1][2:].split(",")[1])} for i in open("input/input_14.txt").read().strip().split("\n")]
field_x,field_y = 101,103
seconds = 100
q1,q2,q3,q4 = 0,0,0,0
final_locations = [{'x': (i['px']+i['vx']*seconds) % field_x,
                    'y': (i['py']+i['vy']*seconds) % field_y} for i in input]
for location in final_locations:
    if location['x'] > field_x // 2:
        if location['y'] > field_y // 2:
            q4 += 1
        if location['y'] < field_y // 2:
            q1 += 1
    if location['x'] < field_x // 2:
        if location['y'] > field_y // 2:
            q3 += 1
        if location['y'] < field_y // 2:
            q2 += 1
print(q1 * q2 * q3 * q4)
