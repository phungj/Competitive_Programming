# Python3 program for the above approach
# Taken from https://www.geeksforgeeks.org/calculate-number-of-nodes-between-two-vertices-in-an-acyclic-graph-by-dfs-method/

# Function to return the count of nodes
# in the path from source to destination
def dfs(src, dest, vis, adj):
    # Mark the node visited
    vis[src] = 1

    # If dest is reached
    if (src == dest):
        return 1

    # Traverse all adjacent nodes
    for u in adj[src]:

        # If not already visited
        if not vis[u]:
            temp = dfs(u, dest, vis, adj)

            # If there is path, then
            # include the current node
            if (temp != 0):
                return temp + 1

    # Return 0 if there is no path
    # between src and dest through
    # the current node
    return 0


# Function to return the
# count of nodes between two
# given vertices of the acyclic Graph
def countNodes(V, E, src, dest, edges):
    # Initialize an adjacency list
    adj = [[] for i in range(V + 1)]

    # Populate the edges in the list
    for i in range(E):
        adj[edges[i][0]].append(edges[i][1])
        adj[edges[i][1]].append(edges[i][0])

    # Mark all the nodes as not visited
    vis = [0] * (V + 1)

    # Count nodes in the path from src to dest
    count = dfs(src, dest, vis, adj)

    # Return the nodes between src and dest
    return count - 2


n = int(input())
graph = []

for i in range(n - 1):
    current_edge = input().split(" ")
    graph.append([int(vertex) for vertex in current_edge])

lengths = 0

for i in range(1, (n // 2) + 1):
    current_mult = i * 2

    while current_mult <= n:
        lengths += countNodes(n, n - 1, i, current_mult, graph) + 2
        current_mult += i

print(lengths)
