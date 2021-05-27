def topological_sort_Kahn(graph):
    n = graph.get_order()
    in_degree = [0] * n
    for i in range(n):
        successors = graph.get_successors(i)
        for j in successors:
            in_degree[j] += 1
    queue = []
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    visited = 0
    list = []
    while queue:
        v = queue.pop(0)
        list.append(v)
        successors = graph.get_successors(v)
        for i in successors:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)
        visited += 1
    if visited != n:
        return False
    else:
        return list
