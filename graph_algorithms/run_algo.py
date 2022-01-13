from graph_algorithms.bellman_ford import bellman_ford
from graph_algorithms.bfs import bfs
from graph_algorithms.dfs import dfs
from graph_algorithms.dijkstra import dijkstra
from graph_algorithms.kruskal import kruskal
from graph_algorithms.prim import prim


def run_algo(x, start_vertex, des_vertex, graph_type, algo_type):
    """Run algorithms.
       Return graph, result, graph type, path, code error.
       Path consists of 2 elements: a list of vertices traversed and a cost"""

    path = []

    try:
        if algo_type == 0:
            code_error, result = bfs(x, start_vertex, graph_type)
        if algo_type == 1:
            code_error, result = dfs(x, start_vertex, graph_type)
        if algo_type == 2:
            tmp = dijkstra(x, start_vertex, des_vertex, graph_type)
            path = (tmp[0], tmp[1])
            code_error = tmp[2]
            result = tmp[3]

        if algo_type == 3:
            tmp = bellman_ford(x, start_vertex, des_vertex, graph_type)
            path = (tmp[0], tmp[1])
            code_error = tmp[2]
            if code_error == 9 and graph_type == 0:
                code_error = 10
            result = tmp[3]

        if algo_type == 4:
            code_error, result = prim(x, start_vertex, graph_type)
        if algo_type == 5:
            code_error = 0
            result = kruskal(x, graph_type)
        return (x, result, graph_type, path, code_error)
    except:
        return x, result, graph_type, path, 12