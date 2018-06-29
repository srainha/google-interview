import Graph

def detect_cycle(graph):
    visited = set()
    for node in graph.get_nodes():
        if (dfs_check_cycle(graph, node, [], visited)):
            return True
    return False

def dfs_check_cycle(graph, node, current_path, visited):
    if (node in current_path): return True
    if (node in visited): return False
    current_path.append(node)
    visited.add(node)
    next_nodes = graph.get_neighbors(node)
    for next_node in next_nodes:
        if (dfs_check_cycle(graph, next_node, current_path.copy(), visited)):
            return True
    return False

def graph_find_path(graph, start, end, path=[]):
    path += [start]
    if (start == end):
        return path
    for child in graph.get_children(start):
        new_path = graph_find_path(graph, child, end, path.copy())
        if (new_path is not None):
            return new_path
    return None

def graph_shortest_path(graph, start, end): 
    parents = { start : None } # child : parent
    frontier = [start]
    while (frontier != []):
        current = frontier.pop(0)
        if (current == end):
            path = []
            while (parents[current] is not None):
                
        children = graph.get_children(current):
        for child in children:
            if (child not in parents): # not yet visited
                parents[child] = current
                frontier.append(child)
    return None
