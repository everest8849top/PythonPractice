"""
Reorder Routes to Make All Paths Lead to the City Zero
In the problem of reordering routes to make all paths lead to city zero,\
    you will be given an array of connections between cities in pairs of integers.\
    Each connection will show a one-way route from one city to another. \
    For example, [1, 0] means that there is a one-way road from city 1 to city 0. \
    Your task is to reorder the connections such that each city can be reached from city 0, \
    directly or indirectly. The output value should return the minimum number of edges changed.

Here’s an example of the input and output values of this problem:

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]] | Output = 2
In the above example, the output is 2 because we need to reverse two connections to make all \
    paths lead to city zero.
"""

from collections import defaultdict


def minReorder(n, connections):
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append((v, 1))
        graph[v].append((u, 0))

    def dfs(node):
        nonlocal total
        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                total += cost
                dfs(neighbor)

    total = 0
    visited = set()
    dfs(0)
    return total


n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
print(minReorder(n, connections))
