def graph_search(graph,start,goal):
    frontier = [[start]] #store paths

    while frontier:
        path = frontier.pop(0) #select and remove a path
        node = path[-1]

        if node == goal:
            return path
        
        for neighbor in graph.get(node,[]):
            new_path = path + [neighbor]
            frontier.append(new_path)

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

result = graph_search(graph, 'A', 'E')
print(result)