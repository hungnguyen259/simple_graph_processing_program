import networkx as nx


def bellman_ford(x, start, end, graph_type):
    """Bellman-Ford algorithm
    to find the shortest path on the directed graph with no negative cycles"""
    """The function returns the path, cost, error code and result.
       If error code is 7, the starting vertex or destination vertex is not in the graph.
       If error code is 9, the graph has negative cycles.
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

    # distance is the distance from the starting vertex to another vertex
    distance = {}
    # prev is previous vertex
    prev = {}
    for node in x.nodes():
        distance[node] = float('inf')
        prev[node] = node
    distance[start] = 0

    # find the shortest path (on a graph without negative cycles)
    for _ in range(1, len(x.nodes)):
        for node in x.nodes():
            for neighbor in x.neighbors(node):
                if distance[node] + x.adj[node][neighbor]['weight'] < distance[neighbor] \
                        and distance[node] != float('inf'):
                    distance[neighbor] = distance[node] + x.adj[node][neighbor]['weight']
                    prev[neighbor] = node

    # Check for negative cycles
    # Error code is 9 if the graph has negative cycles
    for node in x.nodes():
        for neighbor in x.neighbors(node):
            if distance[node] + x.adj[node][neighbor]['weight'] < distance[neighbor] \
                    and distance[node] != float('inf'):
                return [], 0, 9, result

    # Find the shortest path by tracing from end to start
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
