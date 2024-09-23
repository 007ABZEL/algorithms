from collections import deque
import heapq

def dfs(graph, start, visited=None):
    """
    Explores a graph using the Depth-First Search (DFS) algorithm.

    Args:
        graph (dict): A dictionary representing the graph. Keys are nodes, and values are lists of adjacent nodes.
        start: The node to start the search from.
        visited (set, optional): A set of visited nodes. Defaults to None.

    Returns:
        None
    """

    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    """
    Explores a graph using the Breadth-First Search (BFS) algorithm.

    Args:
        graph (dict): A dictionary representing the graph. Keys are nodes, and values are lists of adjacent nodes.
        start: The node to start the search from.

    Returns:
        None
    """
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')

def dijkstra(graph, start):
    """
    Finds the shortest paths from the start node to all other nodes in a weighted graph using Dijkstra's algorithm.

    Args:
        graph (dict): A dictionary representing the graph. Keys are nodes, and values are lists of tuples (neighbor, weight).
        start: The node to start the search from.

    Returns:
        dict: A dictionary where keys are nodes and values are the shortest distance from the start node.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

distances = dijkstra(graph, 'A')
print(distances)
