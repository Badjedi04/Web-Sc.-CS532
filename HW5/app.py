from flask import Flask, render_template, request, jsonify
import networkx as nx
import json

app = Flask(__name__)

# load karate club graph
G = nx.karate_club_graph()

# get node attributes
node_attr = nx.get_node_attributes(G, "club")

# convert graph to D3.js-compatible JSON format
json_graph = {
    "nodes": [{"id": str(n), "club": node_attr[n]} for n in G.nodes()],
    "links": [{"source": str(u), "target": str(v)} for u, v in G.edges()]
}
with open("karate_club.json", "w") as f:
    json.dump(json_graph, f)

@app.route("/")
def index():
    return render_template("directed_graph.html")

@app.route("/split_graph")
def split_graph():
    # load graph after split
    with open('static/' + "split_graph_to_two.json", "r") as f:
        json_graph = json.load(f)
    return jsonify(json_graph)

@app.route("/karate_club")
def karate_club():
    # load original graph
    with open('static/' + "original.json", "r") as f:
        json_graph = json.load(f)
    return jsonify(json_graph)

if __name__ == "__main__":
    app.run(debug=True)
