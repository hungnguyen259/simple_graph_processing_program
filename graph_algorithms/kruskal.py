import networkx as nx


def trace_root(trace, target):
    """Use recursion to trace root in a disjoint set"""

    if trace[target] != target:
        return trace_root(trace, trace[target])
    return target


def union(trace, rank, node_1, node_2):
    root_1 = trace_root(trace, node_1)
    root_2 = trace_root(trace, node_2)
    if rank[root_1] < rank[root_2]:
        trace[root_1] = root_2
    elif rank[root_1] > rank[root_2]:
        trace[root_2] = root_1
    else:
        trace[root_2] = root_1
        rank[root_1] += 1


def kruskal(x, graph_type):
    """Kruskal's Algorithm to find the minimum spanning tree.
    Return spanning tree"""

    # use dictionary to sort edges by weight
    d = {}
    for i in x.nodes:
        for j in x.adj[i]:
            # get all edges
            if f'{j}-{i}' not in d.keys():
                d[f'{i}-{j}'] = x.adj[i][j]['weight']
    sort_edge_by_weight = sorted(d.items(), key=lambda y: y[1])

    # use trace to detect cycle
    trace = {}
    rank = {}
    result = []

    count = 0
    for i in x.nodes:
        trace[i] = i
        rank[i] = 0

    for i in sort_edge_by_weight:
        parent = i[0].split('-')[0]
        child = i[0].split('-')[1]

        # first check disjoint set
        # if it already has indicated cycle
        # trace_root function will go to infinite loops
        if trace_root(trace, parent) != trace_root(trace, child):
            # if we trace back to the root of the tree
            # and it indicates no cycle
            # we update the disjoint set and add edge into result
            count = count + 1
            result.append([parent, child, i[1]])
            union(trace, rank, parent, child)
        if count == len(x.nodes) - 1:
            break

    # create minimum spanning tree
    if graph_type == 0:
        spanning_tree = nx.Graph()
    else:
        spanning_tree = nx.DiGraph()

    for i in result:
        spanning_tree.add_node(i[0])
        spanning_tree.add_node(i[1])
        spanning_tree.add_edge(i[0], i[1], weight=x.adj[i[0]][i[1]]['weight'])
    return spanning_tree
