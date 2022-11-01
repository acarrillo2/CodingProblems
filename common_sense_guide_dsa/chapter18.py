"""
Chapter 18 exercises of "A Common-Sense Guide to Data Structures and Algorithms"
"""
from queue import SimpleQueue

class GraphNode:
    def __init__(self, name):
        self.name = name
        self.adjacent_nodes = []
    
    def add_adjacent_node(self, node):
        self.adjacent_nodes.append(node)

def build_family_tree():
    anne = GraphNode("Anne")
    mary_anne = GraphNode("Mary Anne")
    alice = GraphNode("Alice")
    julie = GraphNode("Julie")
    christy = GraphNode("Christy")
    beth = GraphNode("Beth")
    cameron = GraphNode("Cameron")
    austin = GraphNode("Austin")
    gabriel = GraphNode("Gabriel")
    tonio = GraphNode("Tonio")

    anne.adjacent_nodes = [mary_anne, alice]
    mary_anne.adjacent_nodes = [anne, julie, christy, beth]
    julie.adjacent_nodes = [mary_anne]
    christy.adjacent_nodes = [mary_anne]
    beth.adjacent_nodes = [mary_anne]
    alice.adjacent_nodes = [anne, cameron, austin, gabriel, tonio]
    cameron.adjacent_nodes = [alice]
    austin.adjacent_nodes = [alice]
    gabriel.adjacent_nodes = [alice]
    tonio.adjacent_nodes = [alice]
    return anne

def build_social_network():
    idris = GraphNode("Idris")
    talia = GraphNode("Talia")
    kamil = GraphNode("Kamil")
    lina = GraphNode("Lina")
    ken = GraphNode("Ken")
    marco = GraphNode("Marco")
    sasha = GraphNode("Sasha")

    idris.adjacent_nodes = [kamil, talia]
    talia.adjacent_nodes = [ken, idris]
    kamil.adjacent_nodes = [idris, lina]
    lina.adjacent_nodes = [kamil, sasha]
    ken.adjacent_nodes = [talia, marco]
    marco.adjacent_nodes = [ken, sasha]
    sasha.adjacent_nodes = [lina, marco]
    return idris, lina

def find_name_breadth_first_search(name, graph):
    visited_nodes = {}
    visited_nodes[graph.name] = True
    queue = SimpleQueue()
    queue.put(graph)

    while queue.qsize() > 0:
        current = queue.get()
        print(current.name)
        if current.name == name:
            return name
        for i in current.adjacent_nodes:
            if i.name not in visited_nodes:
                queue.put(i)
                visited_nodes[i.name] = True



def find_shortest_path(start_node, end_node):
    if start_node.name == end_node.name:
        return [start_node]

    shortest_path = []
    current_path = []
    for i in start_node.adjacent_nodes:
        current_path.append(start_node.name)
        visited_nodes = {}
        visited_nodes[start_node.name] = True
        queue = SimpleQueue()
        queue.put(i)
        while queue.qsize() > 0:
            current = queue.get()
            print(current.name)
            current_path.append(current.name)
            if current.name == end_node.name:
                if len(shortest_path) == 0 or len(shortest_path) > len(current_path):
                    shortest_path = current_path
                current_path = []
            for i in current.adjacent_nodes:
                if i.name not in visited_nodes:
                    queue.put(i)
                    visited_nodes[i.name] = True
        current_path = []
    return shortest_path

def main():
    print("Testing")
    graph = build_family_tree()
    print("Found " + str(find_name_breadth_first_search("Austin", graph)))

    idris, lina = build_social_network()
    print(find_shortest_path(idris, lina))


main()