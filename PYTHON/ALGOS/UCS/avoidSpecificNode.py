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
        self.nodes[to_node].add_neighbor(from_node, cost)

class UniformCostSearch:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal, blocked=set()):  # ← new parameter
        distance = {node: float('inf') for node in self.graph.nodes}
        distance[start] = 0
        parent = {node: None for node in self.graph.nodes}
        pq = [(0, start)]

        while pq:
            curr_cost, current = heapq.heappop(pq)

            if current in blocked:   # ← skip blocked nodes
                continue

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


g = Graph()
for u, v, c in [('A','B',2),('A','C',4),('B','D',7),('B','E',1),('C','E',3),('D','E',2)]:
    g.add_edge(u, v, c)

ucs = UniformCostSearch(g)

path, cost = ucs.search('A', 'D', blocked=set())
print("No block  —", path, cost)      # ['A','B','E','D'], 5

path, cost = ucs.search('A', 'D', blocked={'E'})
print("Block E   —", path, cost)      # ['A','B','D'], 9  — forced longer route

path, cost = ucs.search('A', 'D', blocked={'E','B'})
print("Block E,B —", path, cost)      # None — D completely unreachable