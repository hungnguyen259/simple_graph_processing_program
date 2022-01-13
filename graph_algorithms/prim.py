import networkx as nx


def prim(x, start, graph_type):
    """Prim algorithm to find a minimum spanning tree.
       Return error code, spanning tree.
       Error code is 6 if starting vertex not in graph."""

    # result initialization
    if graph_type == 0:
        spanning_tree = nx.Graph()
    else:
        spanning_tree = nx.DiGraph()

    # returns error code of 6 if starting vertex not in graph
    if start not in x.nodes():
        return 6, spanning_tree

    # initialize
    queue = {start: 0}

    # previous vertex
    prev = {start: start}

    # result is the list of vertices we have visited
    result = []

    # pop the edge with the smallest weight
    while queue:

        node = min(queue, key=queue.get)
        queue.pop(node)
        result.append(node)
        x.nodes[node]['visited'] = 1

        # add unvisited neighbor vertices to queue
        for neighbor in x.neighbors(node):
            if neighbor not in queue and x.nodes[neighbor]['visited'] == 0:
                queue[neighbor] = x.adj[node][neighbor]['weight']
                prev[neighbor] = node

            # update the smaller weight in queue
            if neighbor in queue and queue[neighbor] > x.adj[node][neighbor]['weight']:
                queue[neighbor] = x.adj[node][neighbor]['weight']
                prev[neighbor] = node

    # create minimum spanning tree
    for i in result:
        if i != start:
            spanning_tree.add_node(prev[i])
            spanning_tree.add_node(i)
            spanning_tree.add_edge(prev[i], i, weight=x.adj[prev[i]][i]['weight'])

    return 0, spanning_tree
