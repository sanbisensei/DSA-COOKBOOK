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

    def search(self, start, goals):  # goals is now a SET
        goals = set(goals)           # ensure it's a set

        distance = {node: float('inf') for node in self.graph.nodes}
        distance[start] = 0
        parent = {node: None for node in self.graph.nodes}
        pq = [(0, start)]

        goal_found = None  # ← track WHICH goal was reached

        while pq:
            curr_cost, current = heapq.heappop(pq)

            if current in goals:   # ← only change from base: "in goals" not "== goal"
                goal_found = current
                break

            for neighbor, edge_cost in self.graph.nodes[current].neighbors.items():
                new_cost = curr_cost + edge_cost
                if new_cost < distance[neighbor]:
                    distance[neighbor] = new_cost
                    parent[neighbor] = current
                    heapq.heappush(pq, (new_cost, neighbor))

        if goal_found is None:
            return None, float('inf'), None

        path = []
        node = goal_found
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()

        return path, distance[goal_found], goal_found


g = Graph()
for u, v, c in [('A','B',2),('A','C',4),('B','D',7),('B','E',1),('C','E',3),('D','E',2)]:
    g.add_edge(u, v, c)

ucs = UniformCostSearch(g)
path, cost, found = ucs.search('A', {'D', 'C'})
print("Path:", path)
print("Cost:", cost)
print("Goal reached:", found)