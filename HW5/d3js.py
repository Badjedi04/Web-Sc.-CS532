import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import json

def dump_graph_to_json(graph, filename):
    """
    Converts a NetworkX graph into a JSON object and saves it to a file.

    Args:
        graph: A NetworkX graph object.
        filename: The name of the output file (without the '.json' extension).
    """
    nodes = []
    links = []
    club_labels = nx.get_node_attributes(graph, 'club')

    for node in graph.nodes():
        if club_labels[node] == 'Mr. Hi':
            group = 'A'
        else:
            group = 'B'
        nodes.append({'id': node, 'group': group})

    for edge in graph.edges():
        start, end = edge
        value = graph.degree(start)  
        links.append({'source': start, 'target': end, 'value': value})

    graph_data = {'nodes': nodes, 'links': links}

    with open('static/' + filename + '.json', 'w') as outfile:
        json.dump(graph_data, outfile)

initial_graph = nx.karate_club_graph()

dump_graph_to_json(initial_graph, 'original')

club_labels = nx.get_node_attributes(initial_graph, 'club')
color_map = {'Mr. Hi': 'red', 'John': 'blue'}
node_colors = [color_map[club_labels[node]] for node in initial_graph.nodes()]

plt.figure(figsize=(8, 8))
nx.draw(initial_graph, pos=nx.spring_layout(initial_graph), with_labels=True, node_color=node_colors, node_size=400)
plt.show()

target_cluster_count = 2
iteration_count = 0
while (initial_graph.number_of_edges() >= 1 and nx.algorithms.number_connected_components(initial_graph) < target_cluster_count):
    betweenness_centrality = nx.edge_betweenness_centrality(initial_graph)
    max_betweenness = max(betweenness_centrality.values())
    edge_to_remove = [edge for edge, centrality in betweenness_centrality.items() if centrality == max_betweenness][0]

    initial_graph.remove_edge(*edge_to_remove)
    club_labels = nx.get_node_attributes(initial_graph, 'club')
    node_colors = [color_map[club_labels[node]] for node in initial_graph.nodes()]

    plt.figure(figsize=(8, 8))
    nx.draw(initial_graph, pos=nx.spring_layout(initial_graph), with_labels=True, node_color=node_colors, node_size=400)
    plt.show()

    iteration_count += 1
    cluster_count = nx.algorithms.number_connected_components(initial_graph)
    if cluster_count == target_cluster_count:
        dump_graph_to_json(initial_graph, 'split_graph_to_two')

print('Total iterations to split the graph:', iteration_count)
