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


def dijkstra(Grafo, salida):
    dist, prev = {}, {}
    result = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    Q = [vertice for vertice in Grafo]

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        result.append(u)

        for vecino in Grafo[u]:
            if vecino in Q and dist[vecino] > dist[u] + Grafo[u][vecino]['weight']:
                dist[vecino] = dist[u] + Grafo[u][vecino]['weight']
                prev[vecino] = u

    return result, dist, prev

start_time = time.time()
s, distancia, previos = dijkstra(G, '0')
print(f"{s=}")
print(f"{distancia=}")
print(f"{previos=}")

print("--- %s seconds ---" % (time.time() - start_time))