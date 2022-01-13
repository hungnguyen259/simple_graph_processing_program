import graphviz
from PIL import Image


def output(x, result, graph_type):
    """ Draw the graph and save it as a png file"""
    if graph_type == 0:
        dot = graphviz.Graph(format = 'png')
    else:
        dot = graphviz.Digraph(format='png')

    for node in x.nodes():
        dot.node(node, node)

    color = ['black', 'red']
    red_edges = result.edges

    for edge in x.edges():
        if edge in red_edges:
            dot.edge(edge[0], edge[1], color=color[1], label=str(x.adj[edge[0]][edge[1]]['weight']))
        else:
            dot.edge(edge[0], edge[1], color=color[0], label=str(x.adj[edge[0]][edge[1]]['weight']))
    dot.render('graph_image')

    #Resize the png
    image = Image.open('graph_image.png')
    image.thumbnail((420,420))
    image.save('graph_image.png')

