def explore(gardens,cell_type,x,y,plot_fields,edges):
    if not gardens[y][x]['free']:
        return
    if cell_type != gardens[y][x]['type']:
        return
    gardens[y][x]['free'] = False
    if (x,y) in plot_fields:
        return
    plot_fields.append((x,y))
    edges.append(('h',x,y))
    edges.append(('v',x,y))
    edges.append(('h',x+1,y))
    edges.append(('v',x,y+1))
    for direction in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= x + direction[0] < len(gardens[0]) and 0 <= y + direction[1] < len(gardens):
            explore(gardens,cell_type,x + direction[0],y + direction[1],plot_fields,edges)


gardens = [[{'type': field, 'free': True} for field in line] for line in open("input/input_12.txt").read().strip().split("\n")]
plots = []

for row in enumerate(gardens):
    for cell in enumerate(row[1]):
        plot_fields = []
        edges = []
        if cell[1]['free']:
            explore(gardens,cell[1]['type'],cell[0],row[0],plot_fields,edges)
            real_edges = [edge for edge in edges if edges.count(edge) < 2]
            plots.append({'fields': plot_fields,'edges': real_edges})

print(sum([(len(a['fields']) * len(a['edges'])) for a in plots]))