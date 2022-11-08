import networkx as nx
import matplotlib.pyplot as plt


# https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.add_edge.html?highlight=add_edge#networkx.DiGraph.add_edge
# Note: The nodes u and v will be automatically added if they are not already in the graph.
nodes = []
numberOfArista = []
n = int(input(("Número de nodos a ingresar: ")))




def agregar_arista(G, u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)

    # Si el grafo no es dirigido
    if not di :
        # Agrego otra arista en sentido contrario
        G.add_edge(v, u, weight=w)


if __name__ == '__main__':
    # Instantiate the DiGraph
   

    G = nx.DiGraph()
    i=0
    count = 0 
    
    for j in range(n):
        
        nodes.append(input(f"Nombre del nodo num {count}: "))
        numberOfArista.append(int(input(f"Numero de aristas que tiene el nodo {nodes[i]}: ")))
        count+=1

    for n in range (len(numberOfArista)):
        k=0
        for x in range(numberOfArista[i]):
         ai = nodes[i]
         #ai = input(f"Arista {k} inicial del nodo {nodes[i]}: ")
         af = input(f"Arista {k} destino del nodo {nodes[i]}: ")
         weight = int(input(f"Peso de la arista {ai}-{af}: "))
         
         agregar_arista(G, ai, af, weight)
         k+=1 
        i+=1
      
    
         
            

    # Draw the networks
    pos = nx.layout.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo con NetworkX")
    plt.show()

#
#
#for i in range(0, n):
#    ele = int(input())
#
#    lst.append(ele)
#
#print(lst)
#
#
#e = int(input("Enter number of edges related to node: "))
#for i in range(0, n ):
#    ele = int(input())
#    lst.append(ele)


