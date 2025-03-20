## AUTHOR: Ryan Trinh  
## LICENSE: MIT License  
## CONTACT: rtrinh02@csu.fullerton.edu  
## main.py

def find(parent, x):
    """
    Function to find the root of x using path compression.
    :param parent: Dictionary containing parent pointers for each node.
    :param x: The node to find the root of.
    :return: The root of x.
    """
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    """
    Function to perform the union of the sets that x and y belong to.
    :param parent: Dictionary containing parent pointers for each node.
    :param x: First node.
    :param y: Second node.
    """
    root_x = find(parent, x)
    root_y = find(parent, y)
    parent[root_y] = root_x

def detect_cycle(edges):
    """
    Function to detect a cycle in the given list of edges.
    :param edges: List of tuples representing the movements (edges) between coordinates.
    :return: "Loop detected" if a cycle exists, otherwise "No loop detected".
    """
    parent = {}

    for u, v in edges:
        if u not in parent:
            parent[u] = u
        if v not in parent:
            parent[v] = v

    for u, v in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)
        if root_u == root_v:
            return "Loop detected"
        union(parent, root_u, root_v)

    return "No loop detected"

# Sample Test Cases

# Sample 1:
edges1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 2), (4, 6)]
print("Sample 1 Output:", detect_cycle(edges1))  # Expected: Loop detected

# Sample 2:
edges2 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print("Sample 2 Output:", detect_cycle(edges2))  # Expected: No loop detected

