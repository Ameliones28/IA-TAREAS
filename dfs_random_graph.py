import matplotlib.pyplot as plt
import networkx as nx
import random
import time

def agregar_arista(G, u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)

    # Si el grafo no es dirigido
    if not di :
        # Agrego otra arista en sentido contrario
        G.add_edge(v, u, weight=w)

nodes = []
numberOfArista = []

G = nx.DiGraph()

n_nodes = random.randint(40, 50)
for j in range(n_nodes):
    
    for x in range(random.randint(0, 5)):
        ai = str(j)
        af = ai
        while(af==ai):
            af = str(random.randint(0, n_nodes))
        
        weight = random.randint(1,10)
        agregar_arista(G, ai, af, weight)
      

pos = nx.layout.circular_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo con NetworkX")
plt.show()


def dfs(graph, node):
    visited = []
    dist, prev = {}, {}

    for vertice in graph:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[node] = 0

    def transverse(node, father):
        if node not in visited:
            visited.append(node)
            if(node!=father):
                dist[node] = dist[father] + graph[father][node]['weight']
                prev[node] = father
            for neighbour in graph[node]:
                transverse(neighbour, node)
    
    transverse(node, node)                

    return visited, dist, prev


start_time = time.time()
s, distancia, previos = dfs(G, '0')
print(f"{s=}")
print(f"{distancia=}")
print(f"{previos=}")
print("--- %s seconds ---" % (time.time() - start_time))