import networkx as nx


def bfs(x, node, graph_type):
    """bfs algorithm.
    Return error code, result.
    Error code is 6 if starting vertex not in graph.
    Error code is 0 if the algorithm execution is error-free"""

    # result initialization
    if graph_type == 0:
        result = nx.Graph()
    else:
        result = nx.DiGraph()

    # returns error code of 6 if starting vertex not in graph
    if node not in x.nodes():
        return 6, result

    # initialize
    queue = [node]
    x.nodes[node]['level'] = 0
    prev = {}
    for node in x.nodes():
        prev[node] = node

    # BFS
    while queue:
        node = queue.pop(0)
        x.nodes[node]['visited'] = 1
        # print('Visited',node)

        for neighbor in x.neighbors(node):

            # visit neighbors that have not been visited before
            if x.nodes[neighbor]['visited'] == 0 and neighbor not in queue:
                queue.append(neighbor)
                prev[neighbor] = node

    # Create result by tracing
    for node in x.nodes():
        result.add_node(node)
        if prev[node] != node:
            result.add_edge(prev[node], node, weight=x.adj[prev[node]][node]['weight'])

    return 0, result
