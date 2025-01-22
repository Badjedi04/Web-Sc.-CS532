import networkx as nx
import matplotlib.pyplot as plt

# Create an empty directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("B", "D")
G.add_edge("C", "A")
G.add_edge("C", "E")
G.add_edge("E", "C")
G.add_edge("E", "G")
G.add_edge("F", "E")
G.add_edge("H", "G")
G.add_edge("I", "A")
G.add_edge("I", "M")
G.add_edge("I", "N")
G.add_edge("J", "K")
G.add_edge("L", "D")
G.add_edge("M", "D")

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()
