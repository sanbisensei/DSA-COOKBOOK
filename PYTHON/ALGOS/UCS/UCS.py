import heapq


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {} 

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def add_edge(self, from_node, to_node, cost):
        self.add_node(from_node)
        self.add_node(to_node)
        self.nodes[from_node].add_neighbor(to_node, cost)
        self.nodes[to_node].add_neighbor(from_node, cost)  # Undirected



class UniformCostSearch:
    def __init__(self, graph):
        self.graph = graph


    def search(self, start, goal):
        

        distance = {node: float('inf') for node in self.graph.nodes}
        distance[start] = 0
        
        parent = {node: None for node in self.graph.nodes}

        pq = [(0,start)]
        
        while pq:
            curr_cost, current = heapq.heappop(pq)
            
            
            if current == goal:
                break

            
            for neighbor, edge_cost in self.graph.nodes[current].neighbors.items():
                new_cost = curr_cost + edge_cost

              
                if new_cost < distance[neighbor]:
                    distance[neighbor] = new_cost
                    parent[neighbor] = current
                    heapq.heappush(pq, (new_cost, neighbor))

        
        if distance[goal] == float('inf'):
            return None, float('inf')

        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()

        return path, distance[goal]


# Create graph
# g = Graph()
# edges = [
#     ('A', 'B', 2),
#     ('A', 'C', 4),
#     ('B', 'D', 7),
#     ('B', 'E', 1),
#     ('C', 'E', 3),
#     ('D', 'E', 2)
# ]
# for u, v, c in edges:
#     g.add_edge(u, v, c)

# # Run UCS
# ucs = UniformCostSearch(g)
# path, cost ,visited= ucs.search('A', 'D')

# print("Optimal Path:", path)
# print("Total Cost:", cost)
# print("VISITED : ", visited)

g = Graph()
edges = [
    ('A', 'B', 2),
    ('A', 'C', 4),
    ('B', 'C', 1),   # A, B, C are all connected to each other
    ('D', 'E', 3),   # D and E are isolated — no connection to A/B/C
]
for u, v, c in edges:
    g.add_edge(u, v, c)

ucs = UniformCostSearch(g)

# Reachable — should work normally
path, cost = ucs.search('A', 'C')
print(path, cost)          # ['A', 'B', 'C'], 3

# Unreachable — this is where Q3 check triggers
path, cost = ucs.search('A', 'D')
print(path, cost)          # None, inf

# Unreachable the other way too
path, cost = ucs.search('D', 'A')
print(path, cost)          # None, inf