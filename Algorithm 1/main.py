## AUTHOR: Ryan Trinh  
## LICENSE: MIT License  
## CONTACT: rtrinh02@csu.fullerton.edu  
## main.py

#it returns the root of the set containing x
def find(parent, x):

    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
#the union function merges the sets containing elements x and y
def union(parent, x, y):
# find the roots for x and y
    root_x = find(parent, x)
    root_y = find(parent, y)
    parent[root_y] = root_x
# the detect_cycle function uses the union-find algo to detect cycles in an undirected graph
def detect_cycle(edges):

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

