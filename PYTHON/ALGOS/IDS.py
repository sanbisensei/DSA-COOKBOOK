class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self,u,v):
        
        if u not in self.graph:
            self.graph[u] = []

        self.graph[u].append(v)

    def dls(self,node,goal,limit,path):

        path.append(node)
        print(f"\nVisiting: {node} in Depth {limit}")

        if node == goal:
            return True

        if limit <= 0:
            path.pop()
            return False
            
        for neighbor in self.graph.get(node,[]):
            if self.dls(neighbor,goal,limit-1,path):
                return True
            
        # backtrack
        path.pop()
        return False



    def ids(self,start,goal,Max_Depth):

        for Depth in range(Max_Depth+1):

            print(f"\nIteration starts with Depth limit: {Depth}")

            path = []

            found = self.dls(start,goal,Depth,path)

            if found:
                print(f"\n{goal} found in Depth Limit: {Depth}")
                return path
            
        print("Goal not found in anywhere in any path")
        return None
          


if __name__ == "__main__":

    g = Graph()
    g.add_edge('A','B')
    g.add_edge('A','C')
    g.add_edge('B','D')
    g.add_edge('B','E')
    g.add_edge('C','F')


    result = g.ids('A','F',Max_Depth=5)

    if result:
        print(f"\nthe path to the goal is {" > ".join(result)}")