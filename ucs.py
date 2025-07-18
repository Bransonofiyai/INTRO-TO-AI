import heapq

def ucs(graph, start, goal):
    queue = [(0, [start])]
    visited = set()
    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, path + [neighbor]))
    return None, float('inf')

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 3)],
        'D': [],
        'E': [('F', 1)],
        'F': []
    }
    path, cost = ucs(graph, 'A', 'F')
    print(f"UCS path from A to F: {path} with cost {cost}")
