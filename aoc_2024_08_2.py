textinput = open("input/input_08.txt").read()
station_types = set([i for i in textinput]).difference(set(['\n','.']))
station_locations = {s: [(field[0],line[0]) for line in enumerate(textinput.strip().split('\n')) for field in enumerate(line[1]) if field[1] == s ] for s in station_types}
size = (len(textinput.strip().split('\n')[0]),len(textinput.strip().split('\n')))
harmonics = [(0.5+i)*sign for i in range(max(size[0],size[1])+1) for sign in [-1,1]]
interference_locations = [((a[0]+b[0])/2.0 + ((a[0]-b[0]) * d),(a[1]+b[1])/2.0 + (d * (a[1]-b[1]))) for s in station_types for idx,a in enumerate(station_locations[s]) for b in station_locations[s][idx+1:] for d in harmonics]
print(len([il for il in set(interference_locations) if il[0] >= 0 and il[1] >= 0 and il[0]< size[0] and il[1] < size[1]]))