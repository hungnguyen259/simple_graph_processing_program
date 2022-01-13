import networkx as nx


def dijkstra(x, start, end, graph_type):
    """Dijkstra Algorithm to find the shortest path between 2 vertices"""
    """apply to positive weights"""
    """The function returns the path, cost, error code and result. 
       If error code is 7, the starting vertex or destination vertex is not in the graph.
       If error code is 8, the graph has negative weight
       If error code is 11, no path from starting vertex to destination vertex.
       (located in 2 different connected components or no direction from starting vertex to destination vertex)"""

    # result initialization
    if graph_type == 0:
        result = nx.Graph()
    else:
        result = nx.DiGraph()

    # Error code is 7 if the starting vertex or destination vertex is not in the graph.
    if (start not in x.nodes()) or (end not in x.nodes()):
        return [], 0, 7, result

    # Error code is 8 if the graph has negative weight
    for i in x.nodes():
        for j in x.neighbors(i):
            if x.adj[i][j]['weight'] < 0:
                return [], 0, 8, result

    queue = {start: 0}

    # distance is the distance from the starting vertex to another vertex
    # prev is previous vertex
    distance = {}
    prev = {}

    for i in x.nodes:
        distance[i] = float('inf')
        prev[i] = i
    distance[start] = 0

    while len(queue) > 0:
        # pop the vertex with the smallest weight in the queue
        node = min(queue, key=queue.get)
        queue.pop(node)

        for j in x.neighbors(node):
            # check if current vertex can generate optimal path
            if distance[node] + x.adj[node][j]['weight'] < distance[j]:
                distance[j] = distance[node] + x.adj[node][j]['weight']
                prev[j] = node
                if x.nodes[j]['visited'] == 0:
                    queue[j] = distance[j]

        x.nodes[node]['visited'] = 1

    # find the shortest path by tracing from end to start
    # Error code is 11 if there is no path from starting vertex to destination vertex
    path = []
    previous = end
    while prev:
        path.insert(0, previous)
        if previous == start:
            break
        if previous != prev[previous]:
            previous = prev[previous]
        else:
            path = []
            break

    # Create the graph of the results
    if len(path) != 0:
        for node in path:
            result.add_node(node)
        for i in range(len(path) - 1):
            result.add_edge(path[i], path[i + 1], weight=x.adj[path[i]][path[i + 1]]['weight'])
        return path, distance[end], 0, result
    else:
        return path, 0, 11, result
