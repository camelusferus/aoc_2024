def explore(gardens,cell_type,x,y,plot_fields,edges):
    if not gardens[y][x]['free']:
        return
    if cell_type != gardens[y][x]['type']:
        return
    gardens[y][x]['free'] = False
    if (x,y) in plot_fields:
        return
    plot_fields.append((x,y))
    edges.append({'type':'h','x':x,'y':y,'free':True,"topleft": True})
    edges.append({'type':'v','x':x,'y':y,'free':True,"topleft": True})
    edges.append({'type':'h','x':x+1,'y':y,'free':True,"topleft":False})
    edges.append({'type':'v','x':x,'y':y+1,'free':True,"topleft":False})
    for direction in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= x + direction[0] < len(gardens[0]) and 0 <= y + direction[1] < len(gardens):
            explore(gardens,cell_type,x + direction[0],y + direction[1],plot_fields,edges)

def explore_edges(real_edges,type,x,y,topleft):
    filter_edges = [edge for edge in real_edges if (edge['type'] == type and edge['x'] == x and edge['y'] == y and edge['topleft'] == topleft)]
    if len(filter_edges) == 0:
        return
    edge = filter_edges[0]
    if not edge['free']:
        return
    edge['free'] = False
    if edge['type'] == 'h':
        explore_edges(real_edges,type,x,y-1,topleft)
        explore_edges(real_edges,type,x,y+1,topleft)
    else:
        explore_edges(real_edges,type,x+1,y,topleft)
        explore_edges(real_edges,type,x-1,y,topleft)


gardens = [[{'type': field, 'free': True} for field in line] for line in open("input/input_12.txt").read().strip().split("\n")]
plots = []

for row in enumerate(gardens):
    for cell in enumerate(row[1]):
        plot_fields = []
        edges = []
        if cell[1]['free']:
            explore(gardens,cell[1]['type'],cell[0],row[0],plot_fields,edges)
            real_edges = [edge for edge in edges if len([edge_filter for edge_filter in edges if (edge['type'] == edge_filter['type'] and edge['x'] == edge_filter['x'] and edge['y'] == edge_filter['y'])])<2]
            discounted_edges = 0
            for e in real_edges:
                if e['free']:
                    explore_edges(real_edges,e['type'],e['x'],e['y'],e['topleft'])
                    discounted_edges += 1
            plots.append({'fields': plot_fields,'edges': discounted_edges})

print(sum([(len(a['fields']) * a['edges']) for a in plots]))