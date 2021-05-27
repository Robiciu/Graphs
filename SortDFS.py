def topological_sort_help(graph, v, visited, stack):
    visited[v] = True
    successors = graph.get_successors(v)
    for i in successors:
        if not visited[i]:
            topological_sort_help(graph, i, visited, stack)
    stack.append(v)


def topological_sort_DFS(graph):
    n = graph.get_order()
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            topological_sort_help(graph, i, visited, stack)
    return stack[::-1]
