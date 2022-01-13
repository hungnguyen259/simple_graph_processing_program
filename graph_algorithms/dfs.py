import networkx as nx


def dfs(x, node, graph_type):
    """dfs algorithm.
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

    stack = [node]
    prev = {}
    path = []
    for node in x.nodes():
        prev[node] = node

    while stack:

        node = stack.pop()
        if node in path:
            continue
        path.append(node)

        # find children and add to the priority
        for neighbor in x.neighbors(node):
            stack.append(neighbor)
            if neighbor not in path:
                prev[neighbor] = node

    # Create the graph of the results
    for node in x.nodes():
        result.add_node(node)
        if prev[node] != node:
            result.add_edge(prev[node], node, weight=x.adj[prev[node]][node]['weight'])

    return 0, result
