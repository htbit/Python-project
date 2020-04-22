graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

print(dfs(graph, 'A'))
print(dfs(graph, 'B'))
print(dfs(graph, 'C'))
print(dfs(graph, 'D'))
print(dfs(graph, 'E'))
print(dfs(graph, 'F'))