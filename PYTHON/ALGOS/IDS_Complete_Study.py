"""
================================================================
  IDS COMPLETE EXAM STUDY GUIDE
  Iterative Deepening Search — All Variants + 15 Practice Problems
================================================================
"""

# ================================================================
# BASE CODE — Faculty's Original (memorize this perfectly)
# ================================================================

class Graph:
    def __init__(self):
        # Adjacency list representation
        self.graph = {}

    def add_edge(self, u, v):
        """Add edge from u to v"""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dls(self, node, goal, limit, path):
        """Depth-Limited Search"""
        path.append(node)
        print(f"Visiting: {node}, Depth limit: {limit}")

        if node == goal:
            return True

        if limit <= 0:
            path.pop()
            return False

        for neighbor in self.graph.get(node, []):
            if self.dls(neighbor, goal, limit - 1, path):
                return True

        # Backtrack
        path.pop()
        return False

    def ids(self, start, goal, max_depth):
        """Iterative Deepening Search"""
        for depth in range(max_depth + 1):
            print(f"\nIteration with depth limit = {depth}")
            path = []
            found = self.dls(start, goal, depth, path)
            if found:
                print(f"\nGoal '{goal}' found at depth {depth}")
                return path
        print("\nGoal not found within given depth limit")
        return None


# ================================================================
#
# VARIANT 1 — UNDIRECTED GRAPH
#
# WHAT CHANGED: add_edge only
# WHY: Original only stores u→v. Undirected needs v→u too.
# RULE: Any edge means you can travel BOTH ways.
# KEYWORDS that signal undirected: "road", "friendship",
#   "connection between", "mutual", "two-way"
#
# ================================================================

class GraphV1_Undirected:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # --- CHANGE START ---
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:      # NEW: also initialize v
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)      # NEW: reverse edge added
        # --- CHANGE END ---

    # dls and ids are IDENTICAL to base — no changes needed
    def dls(self, node, goal, limit, path):
        path.append(node)
        if node == goal:
            return True
        if limit <= 0:
            path.pop()
            return False
        for neighbor in self.graph.get(node, []):
            if self.dls(neighbor, goal, limit - 1, path):
                return True
        path.pop()
        return False

    def ids(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            path = []
            found = self.dls(start, goal, depth, path)
            if found:
                return path
        return None


# ================================================================
#
# VARIANT 2 — CYCLE DETECTION (Visited Set)
#
# WHAT CHANGED: dls gets a `visited` set parameter; ids passes set()
# WHY: In graphs with cycles (A→B→C→A), without visited,
#      DLS loops infinitely revisiting the same nodes.
# RULE: visited.discard(node) on backtrack — this is crucial.
#       If you don't discard, the next IDS iteration can't
#       re-explore nodes that were visited in the previous one.
# KEYWORDS: "graph with cycles", "undirected graph",
#   "avoid revisiting", "don't repeat nodes"
#
# ================================================================

class GraphV2_CycleDetection:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # undirected

    # --- CHANGE: added `visited` parameter ---
    def dls(self, node, goal, limit, path, visited):
        if node in visited:          # NEW: skip if already seen this iteration
            return False
        visited.add(node)            # NEW: mark as seen
        path.append(node)
        if node == goal:
            return True
        if limit <= 0:
            visited.discard(node)    # NEW: unmark when backtracking
            path.pop()
            return False
        for neighbor in self.graph.get(node, []):
            if self.dls(neighbor, goal, limit - 1, path, visited):
                return True
        visited.discard(node)        # NEW: unmark when backtracking
        path.pop()
        return False

    # --- CHANGE: create fresh visited set each iteration ---
    def ids(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            path = []
            visited = set()          # NEW: fresh set per iteration
            found = self.dls(start, goal, depth, path, visited)
            if found:
                return path
        return None


# ================================================================
#
# VARIANT 3 — COUNT NODES VISITED
#
# WHAT CHANGED: __init__ adds counter; dls increments it;
#               ids resets it before starting
# WHY: Exam may ask "how many nodes does IDS explore?"
# RULE: Increment BEFORE any return. Reset in ids() not __init__
#       so repeated calls give fresh counts.
# KEYWORDS: "count", "how many nodes", "number of expansions"
#
# ================================================================

class GraphV3_CountVisits:
    def __init__(self):
        self.graph = {}
        self.visit_count = 0         # NEW: counter attribute

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dls(self, node, goal, limit, path):
        self.visit_count += 1        # NEW: count every node we enter
        path.append(node)
        if node == goal:
            return True
        if limit <= 0:
            path.pop()
            return False
        for neighbor in self.graph.get(node, []):
            if self.dls(neighbor, goal, limit - 1, path):
                return True
        path.pop()
        return False

    def ids(self, start, goal, max_depth):
        self.visit_count = 0         # NEW: reset before each IDS call
        for depth in range(max_depth + 1):
            path = []
            found = self.dls(start, goal, depth, path)
            if found:
                print(f"Total nodes visited across all iterations: {self.visit_count}")
                return path
        return None


# ================================================================
#
# VARIANT 4 — RETURN DEPTH WITH PATH
#
# WHAT CHANGED: ids returns a tuple (path, depth) instead of path
# WHY: Sometimes you need to know HOW DEEP the goal was found
# RULE: Unpack with: path, depth = g.ids(...)
# KEYWORDS: "return the depth", "at what level",
#   "how deep is the goal", "depth of solution"
#
# ================================================================

class GraphV4_ReturnDepth:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dls(self, node, goal, limit, path):  # unchanged
        path.append(node)
        if node == goal:
            return True
        if limit <= 0:
            path.pop()
            return False
        for neighbor in self.graph.get(node, []):
            if self.dls(neighbor, goal, limit - 1, path):
                return True
        path.pop()
        return False

    def ids(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            path = []
            found = self.dls(start, goal, depth, path)
            if found:
                return path, depth   # NEW: return tuple instead of just path
        return None, -1              # NEW: -1 signals "not found"

# Usage:
#   path, depth = g.ids('A', 'F', 5)
#   print(f"Found at depth {depth}: {path}")


# ================================================================
#
# VARIANT 5 — SORTED (ORDERED) CHILDREN
#
# WHAT CHANGED: one word in dls — sorted() around neighbors
# WHY: Guarantees deterministic, alphabetical exploration order
# RULE: sorted() makes a NEW list — original graph unchanged
#       reverse=True for reverse alphabetical / descending order
# KEYWORDS: "alphabetical order", "sorted", "ordered search",
#   "lexicographic", "smallest first"
#
# ================================================================

class GraphV5_SortedChildren:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dls(self, node, goal, limit, path):
        path.append(node)
        if node == goal:
            return True
        if limit <= 0:
            path.pop()
            return False
        # --- CHANGE: wrap neighbors with sorted() ---
        for neighbor in sorted(self.graph.get(node, [])):  # NEW: sorted
            if self.dls(neighbor, goal, limit - 1, path):
                return True
        path.pop()
        return False

    def ids(self, start, goal, max_depth):  # unchanged
        for depth in range(max_depth + 1):
            path = []
            found = self.dls(start, goal, depth, path)
            if found:
                return path
        return None

# For REVERSE order: sorted(..., reverse=True)
# For numeric priority: sorted(..., key=lambda x: priority[x])


# ================================================================
#
# VARIANT 6 — FIND ALL PATHS
#
# WHAT CHANGED: dls doesn't return True/False anymore — it collects
#               ALL paths into a list. ids returns that list.
# WHY: Sometimes you want every possible route, not just the first
# CRITICAL: list(path) makes a COPY — if you do all_paths.append(path)
#           you store a REFERENCE and all entries will be the same!
# KEYWORDS: "all paths", "every route", "list of paths",
#   "how many ways", "enumerate paths"
#
# ================================================================

class GraphV6_AllPaths:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # --- CHANGE: no return value, takes all_paths list ---
    def dls(self, node, goal, limit, path, all_paths):
        path.append(node)
        if node == goal:
            all_paths.append(list(path))  # NEW: copy path into results
            path.pop()
            return                        # NEW: return, DON'T stop — keep searching!
        if limit <= 0:
            path.pop()
            return
        for neighbor in self.graph.get(node, []):
            self.dls(neighbor, goal, limit - 1, path, all_paths)  # no `if` check
        path.pop()

    # --- CHANGE: ids returns list of paths ---
    def ids(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            all_paths = []               # NEW: collect all paths
            self.dls(start, goal, depth, [], all_paths)
            if all_paths:
                return all_paths         # NEW: return list
        return []


# ================================================================
#
# VARIANT 7 — WEIGHTED EDGES (Cost-limited IDS)
#
# WHAT CHANGED: add_edge stores (neighbor, weight) tuples;
#               dls tracks cumulative cost instead of depth;
#               ids iterates over cost limits instead of depths
# WHY: Real problems have costs — finding cheapest path matters
# RULE: Unpack tuple with: for neighbor, weight in self.graph...
# KEYWORDS: "weighted", "cost", "shortest cost path",
#   "minimum cost", "each edge has weight/distance"
#
# ================================================================

class GraphV7_Weighted:
    def __init__(self):
        self.graph = {}

    # --- CHANGE: add_edge accepts weight ---
    def add_edge(self, u, v, weight=1):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))   # NEW: store as tuple

    # --- CHANGE: cost_limit and cost_so_far replace limit ---
    def dls(self, node, goal, cost_limit, path, cost_so_far):
        path.append(node)
        if node == goal:
            return cost_so_far              # NEW: return actual cost
        if cost_so_far >= cost_limit:       # NEW: cost cutoff
            path.pop()
            return None
        for neighbor, weight in self.graph.get(node, []):  # NEW: unpack tuple
            new_cost = cost_so_far + weight
            result = self.dls(neighbor, goal, cost_limit, path, new_cost)
            if result is not None:
                return result
        path.pop()
        return None

    # --- CHANGE: iterate over cost limits, not depths ---
    def ids(self, start, goal, max_cost):
        for cost_limit in range(1, max_cost + 1):   # NEW: cost-based loop
            path = []
            result = self.dls(start, goal, cost_limit, path, 0)
            if result is not None:
                print(f"Found at cost limit {cost_limit}, total cost: {result}")
                return path
        return None


# ================================================================
# ================================================================
#
#   15 PRACTICE PROBLEMS (with full solutions)
#   Covers: IDS modifications + OOP concepts
#
# ================================================================
# ================================================================

print("\n" + "=" * 60)
print("PRACTICE PROBLEMS")
print("=" * 60)

# ----------------------------------------------------------------
# PROBLEM 1 — Add a method to display the graph
# TESTS: OOP (adding methods), understanding adjacency list
# ----------------------------------------------------------------
print("\n--- Problem 1: display_graph() method ---")
"""
QUESTION: Add a display_graph() method to the Graph class
that prints each node and its neighbors.

Expected output for the sample graph:
  A: ['B', 'C']
  B: ['D', 'E']
  C: ['F']
"""

class GraphP1(Graph):
    def display_graph(self):                       # NEW method
        for node, neighbors in self.graph.items():
            print(f"  {node}: {neighbors}")

g = GraphP1()
g.add_edge('A', 'B'); g.add_edge('A', 'C')
g.add_edge('B', 'D'); g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.display_graph()


# ----------------------------------------------------------------
# PROBLEM 2 — Check if a path exists (return True/False only)
# TESTS: Simplifying IDS, removing path tracking
# ----------------------------------------------------------------
print("\n--- Problem 2: path_exists() — return True/False ---")
"""
QUESTION: Add path_exists(start, goal, max_depth) that returns
True if goal is reachable, False otherwise. No path tracking needed.
"""

class GraphP2(Graph):
    def dls_exists(self, node, goal, limit):       # simplified dls
        if node == goal:
            return True
        if limit <= 0:
            return False
        for neighbor in self.graph.get(node, []):
            if self.dls_exists(neighbor, goal, limit - 1):
                return True
        return False

    def path_exists(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            if self.dls_exists(start, goal, depth):
                return True
        return False

g = GraphP2()
g.add_edge('A', 'B'); g.add_edge('B', 'C')
print("A->C exists:", g.path_exists('A', 'C', 5))   # True
print("A->Z exists:", g.path_exists('A', 'Z', 5))   # False


# ----------------------------------------------------------------
# PROBLEM 3 — IDS with multiple goals (stop at any one)
# TESTS: Modifying goal check, list of goals
# ----------------------------------------------------------------
print("\n--- Problem 3: Multiple goals ---")
"""
QUESTION: Modify IDS so that `goal` can be a LIST of nodes.
Return the path to whichever goal is found first.
"""

class GraphP3(Graph):
    def dls(self, node, goal, limit, path):        # goal is now a list
        path.append(node)
        if node in goal:                           # CHANGED: `in` instead of ==
            return True
        if limit <= 0:
            path.pop()
            return False
        for neighbor in self.graph.get(node, []):
            if self.dls(neighbor, goal, limit - 1, path):
                return True
        path.pop()
        return False

    def ids(self, start, goal, max_depth):         # goal passed as list
        for depth in range(max_depth + 1):
            path = []
            found = self.dls(start, goal, depth, path)
            if found:
                return path
        return None

g = GraphP3()
g.add_edge('A', 'B'); g.add_edge('A', 'C')
g.add_edge('B', 'D'); g.add_edge('C', 'E')
print("First of [D, E]:", g.ids('A', ['D', 'E'], 5))  # finds D or E


# ----------------------------------------------------------------
# PROBLEM 4 — OOP: Subclass that logs every iteration
# TESTS: Inheritance, method overriding
# ----------------------------------------------------------------
print("\n--- Problem 4: Subclass with iteration logging ---")
"""
QUESTION: Create a LoggedGraph class that inherits from Graph
and overrides ids() to print how many nodes were visited
per iteration.
"""

class LoggedGraph(Graph):                          # inherits Graph
    def ids(self, start, goal, max_depth):         # overrides ids
        for depth in range(max_depth + 1):
            path = []
            self._nodes_this_iter = 0              # track per iteration
            found = self.dls_counted(start, goal, depth, path)
            print(f"Depth {depth}: visited {self._nodes_this_iter} nodes")
            if found:
                return path
        return None

    def dls_counted(self, node, goal, limit, path):
        self._nodes_this_iter += 1                 # count this node
        path.append(node)
        if node == goal:
            return True
        if limit <= 0:
            path.pop()
            return False
        for neighbor in self.graph.get(node, []):
            if self.dls_counted(neighbor, goal, limit - 1, path):
                return True
        path.pop()
        return False

g = LoggedGraph()
g.add_edge('A', 'B'); g.add_edge('A', 'C')
g.add_edge('B', 'D'); g.add_edge('C', 'E')
g.ids('A', 'E', 5)


# ----------------------------------------------------------------
# PROBLEM 5 — OOP: __str__ method for Graph
# TESTS: Dunder methods, string representation
# ----------------------------------------------------------------
print("\n--- Problem 5: __str__ and __repr__ ---")
"""
QUESTION: Add __str__ to Graph so print(g) shows the graph
nicely, and __repr__ shows the technical representation.
"""

class GraphP5(Graph):
    def __str__(self):
        lines = ["Graph:"]
        for node in sorted(self.graph):
            lines.append(f"  {node} --> {self.graph[node]}")
        return "\n".join(lines)

    def __repr__(self):
        return f"Graph(nodes={list(self.graph.keys())})"

g = GraphP5()
g.add_edge('A', 'B'); g.add_edge('A', 'C'); g.add_edge('B', 'D')
print(str(g))       # uses __str__
print(repr(g))      # uses __repr__


# ----------------------------------------------------------------
# PROBLEM 6 — OOP: Property for node count
# TESTS: @property decorator, encapsulation
# ----------------------------------------------------------------
print("\n--- Problem 6: @property for node_count ---")
"""
QUESTION: Add a node_count property that returns the number
of unique nodes in the graph. It should be read-only.
"""

class GraphP6(Graph):
    @property
    def node_count(self):                          # @property = read-only attribute
        return len(self.graph)

    @property
    def edge_count(self):
        return sum(len(v) for v in self.graph.values())

g = GraphP6()
g.add_edge('A', 'B'); g.add_edge('A', 'C'); g.add_edge('B', 'D')
print(f"Nodes: {g.node_count}")    # 3 (only source nodes counted)
print(f"Edges: {g.edge_count}")    # 3


# ----------------------------------------------------------------
# PROBLEM 7 — Remove a node from the graph
# TESTS: OOP (adding mutation methods), dict manipulation
# ----------------------------------------------------------------
print("\n--- Problem 7: remove_node() method ---")
"""
QUESTION: Add remove_node(node) that removes the node AND
all edges pointing to it from other nodes.
"""

class GraphP7(Graph):
    def remove_node(self, node):
        # Remove node as a SOURCE (removes all its outgoing edges)
        if node in self.graph:
            del self.graph[node]
        # Remove node as a DESTINATION (removes incoming edges)
        for src in self.graph:
            if node in self.graph[src]:
                self.graph[src].remove(node)

g = GraphP7()
g.add_edge('A', 'B'); g.add_edge('A', 'C'); g.add_edge('B', 'C')
print("Before:", g.graph)
g.remove_node('C')
print("After removing C:", g.graph)


# ----------------------------------------------------------------
# PROBLEM 8 — IDS that avoids a blocked node
# TESTS: Adding constraints to DLS
# ----------------------------------------------------------------
print("\n--- Problem 8: IDS with blocked nodes ---")
"""
QUESTION: Modify IDS to accept a list of `blocked` nodes
that the search must not pass through.
"""

class GraphP8(Graph):
    def dls(self, node, goal, limit, path, blocked):   # NEW: blocked param
        if node in blocked:                            # NEW: skip blocked
            return False
        path.append(node)
        if node == goal:
            return True
        if limit <= 0:
            path.pop()
            return False
        for neighbor in self.graph.get(node, []):
            if self.dls(neighbor, goal, limit - 1, path, blocked):
                return True
        path.pop()
        return False

    def ids(self, start, goal, max_depth, blocked=None):  # NEW: blocked param
        if blocked is None:
            blocked = set()
        for depth in range(max_depth + 1):
            path = []
            found = self.dls(start, goal, depth, path, blocked)
            if found:
                return path
        return None

g = GraphP8()
g.add_edge('A', 'B'); g.add_edge('A', 'C')
g.add_edge('B', 'F'); g.add_edge('C', 'F')
print("Without block:", g.ids('A', 'F', 5))
print("With B blocked:", g.ids('A', 'F', 5, blocked={'B'}))  # must go via C


# ----------------------------------------------------------------
# PROBLEM 9 — OOP: Class method and static method
# TESTS: @classmethod, @staticmethod
# ----------------------------------------------------------------
print("\n--- Problem 9: @classmethod and @staticmethod ---")
"""
QUESTION: Add:
  1. A @staticmethod is_valid_node(node) that returns True if
     node is a string.
  2. A @classmethod from_edge_list(cls, edges) that builds a
     Graph from a list of (u,v) tuples.
"""

class GraphP9(Graph):
    @staticmethod
    def is_valid_node(node):                       # no self or cls
        return isinstance(node, str)

    @classmethod
    def from_edge_list(cls, edges):                # cls = GraphP9
        g = cls()                                  # creates new instance
        for u, v in edges:
            g.add_edge(u, v)
        return g

# Static method — called on class, not instance
print("Is 'A' valid?", GraphP9.is_valid_node('A'))
print("Is 5 valid?",   GraphP9.is_valid_node(5))

# Class method — alternative constructor
edges = [('A','B'), ('A','C'), ('B','D')]
g = GraphP9.from_edge_list(edges)
print("Built from edge list:", g.graph)


# ----------------------------------------------------------------
# PROBLEM 10 — Trace output for given graph (pen-and-paper style)
# TESTS: Understanding DLS recursion and backtracking
# ----------------------------------------------------------------
print("\n--- Problem 10: Trace output ---")
"""
QUESTION: Given edges A→B, B→C, A→D. Run IDS from A to C
with max_depth=3. Write out every "Visiting" line in order.

ANSWER (trace it mentally then verify):
  depth=0: Visiting A(0)
  depth=1: Visiting A(1), B(0)
  depth=2: Visiting A(2), B(1), C(0) ← FOUND
"""

class GraphP10(Graph):
    pass  # use base class as-is

g = GraphP10()
g.add_edge('A', 'B'); g.add_edge('B', 'C'); g.add_edge('A', 'D')
result = g.ids('A', 'C', max_depth=3)
print("Path:", result)


# ----------------------------------------------------------------
# PROBLEM 11 — OOP: Abstract base class
# TESTS: ABC, abstractmethod — advanced OOP
# ----------------------------------------------------------------
print("\n--- Problem 11: Abstract base class for search ---")
"""
QUESTION: Create an abstract base class BaseSearch with an
abstract method search(). Make Graph inherit from it.
"""

from abc import ABC, abstractmethod

class BaseSearch(ABC):                             # abstract base class
    @abstractmethod
    def search(self, start, goal, max_depth):      # must be implemented
        pass

    def display_result(self, path):                # concrete method (shared)
        if path:
            print("Path:", " → ".join(path))
        else:
            print("No path found.")

class GraphP11(BaseSearch, Graph):                 # inherits BOTH
    def __init__(self):
        Graph.__init__(self)                       # call Graph's __init__

    def search(self, start, goal, max_depth):      # implement abstract method
        return self.ids(start, goal, max_depth)

g = GraphP11()
g.add_edge('A', 'B'); g.add_edge('B', 'C')
path = g.search('A', 'C', 5)
g.display_result(path)


# ----------------------------------------------------------------
# PROBLEM 12 — OOP + IDS: Overload __len__ and __contains__
# TESTS: Dunder methods __len__, __contains__
# ----------------------------------------------------------------
print("\n--- Problem 12: __len__ and __contains__ ---")
"""
QUESTION: Add __len__ (returns node count) and __contains__
(returns True if node is in the graph).
"""

class GraphP12(Graph):
    def __len__(self):
        return len(self.graph)                     # len(g) = number of source nodes

    def __contains__(self, node):
        return node in self.graph                  # `node in g` = True/False

g = GraphP12()
g.add_edge('A', 'B'); g.add_edge('A', 'C'); g.add_edge('B', 'D')
print(f"Number of nodes: {len(g)}")       # calls __len__
print(f"'A' in graph: {'A' in g}")        # calls __contains__
print(f"'Z' in graph: {'Z' in g}")


# ----------------------------------------------------------------
# PROBLEM 13 — IDS that returns path length (number of edges)
# TESTS: Post-processing result, understanding path structure
# ----------------------------------------------------------------
print("\n--- Problem 13: Return path length (edges) ---")
"""
QUESTION: Modify ids() to also return the number of edges
in the solution path (path length = nodes - 1).
"""

class GraphP13(Graph):
    def ids(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            path = []
            found = self.dls(start, goal, depth, path)
            if found:
                length = len(path) - 1             # edges = nodes - 1
                return path, length                # return tuple
        return None, 0

g = GraphP13()
g.add_edge('A', 'B'); g.add_edge('A', 'C'); g.add_edge('C', 'F')
path, length = g.ids('A', 'F', 5)
print(f"Path: {path}, Edges: {length}")


# ----------------------------------------------------------------
# PROBLEM 14 — IDS starting from multiple sources
# TESTS: Looping over starts, combining results
# ----------------------------------------------------------------
print("\n--- Problem 14: Multi-source IDS ---")
"""
QUESTION: Add ids_multi_source(starts, goal, max_depth) that
tries IDS from each start node and returns the SHORTEST path found.
"""

class GraphP14(Graph):
    def ids_multi_source(self, starts, goal, max_depth):
        best_path = None
        for start in starts:                       # try each source
            path = self.ids(start, goal, max_depth)
            if path is not None:
                if best_path is None or len(path) < len(best_path):
                    best_path = path               # keep shortest
        return best_path

g = GraphP14()
g.add_edge('A', 'X'); g.add_edge('X', 'Z')       # A→X→Z (length 3)
g.add_edge('B', 'Z')                              # B→Z (length 2)
path = g.ids_multi_source(['A', 'B'], 'Z', 5)
print("Shortest from any start:", path)


# ----------------------------------------------------------------
# PROBLEM 15 — FULL COMBINED: OOP + IDS + All Variants
# TESTS: Everything together — the boss-level problem
# ----------------------------------------------------------------
print("\n--- Problem 15: Full AdvancedGraph class ---")
"""
QUESTION: Create AdvancedGraph that:
  1. Supports both directed and undirected edges
  2. Has cycle detection
  3. Counts total nodes visited
  4. Returns (path, depth, visit_count) from ids()
  5. Has __str__ and __len__
"""

class AdvancedGraph:
    def __init__(self, directed=True):
        self.graph = {}
        self.directed = directed                   # OOP: store mode
        self.visit_count = 0

    def add_edge(self, u, v):
        for node in [u, v]:
            if node not in self.graph:
                self.graph[node] = []
        self.graph[u].append(v)
        if not self.directed:                      # undirected: add reverse
            self.graph[v].append(u)

    def __len__(self):
        return len(self.graph)

    def __str__(self):
        mode = "Directed" if self.directed else "Undirected"
        return f"{mode} Graph with {len(self)} nodes: {list(self.graph.keys())}"

    def dls(self, node, goal, limit, path, visited):
        if node in visited:
            return False
        self.visit_count += 1                      # count visits
        visited.add(node)
        path.append(node)
        if node == goal:
            return True
        if limit <= 0:
            visited.discard(node)
            path.pop()
            return False
        for neighbor in self.graph.get(node, []):
            if self.dls(neighbor, goal, limit - 1, path, visited):
                return True
        visited.discard(node)
        path.pop()
        return False

    def ids(self, start, goal, max_depth):
        self.visit_count = 0                       # reset count
        for depth in range(max_depth + 1):
            path = []
            visited = set()
            if self.dls(start, goal, depth, path, visited):
                return path, depth, self.visit_count   # return triple
        return None, -1, self.visit_count

# Test directed
ag = AdvancedGraph(directed=True)
ag.add_edge('A', 'B'); ag.add_edge('A', 'C'); ag.add_edge('C', 'F')
print(ag)
path, depth, visits = ag.ids('A', 'F', 5)
print(f"Path: {path}, Depth: {depth}, Total visits: {visits}")

# Test undirected (can search backwards!)
ag2 = AdvancedGraph(directed=False)
ag2.add_edge('A', 'B'); ag2.add_edge('A', 'C'); ag2.add_edge('C', 'F')
print(ag2)
path, depth, visits = ag2.ids('F', 'A', 5)      # search backwards!
print(f"Reverse path: {path}, Depth: {depth}, Total visits: {visits}")


# ================================================================
# QUICK REFERENCE — What to change for each question type
# ================================================================
"""
QUESTION TYPE                  |  WHERE TO CHANGE
-------------------------------|--------------------------------
"Undirected graph"             |  add_edge → add reverse edge
"Avoid cycles / loops"         |  dls → add visited set param
"Count nodes visited"          |  __init__ + dls + ids
"Return depth of goal"         |  ids → return (path, depth)
"Alphabetical / sorted order"  |  dls → sorted(neighbors)
"Find ALL paths"               |  dls returns None, collects list
"Weighted edges"               |  add_edge + dls + ids (cost-based)
"Add display/print method"     |  new method, iterate self.graph
"__str__ / print(g)"           |  __str__ dunder
"len(g)"                       |  __len__ dunder
"node in g"                    |  __contains__ dunder
"abstract base class"          |  from abc import ABC, abstractmethod
"@property"                    |  @property decorator, no ()
"alternative constructor"      |  @classmethod + cls()
"utility / helper method"      |  @staticmethod, no self
"subclass / extend"            |  class Child(Parent): + super().__init__()
"blocked / forbidden nodes"    |  dls → check node in blocked
"multiple goals"               |  dls → if node in goal (list)
"multiple start nodes"         |  ids loop over starts list
"""
