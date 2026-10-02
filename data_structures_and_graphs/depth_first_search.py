def dfs(adj_matrix, node_label):
    if node_label < 0 or node_label >= len(adj_matrix):
        return []

    stack = [node_label]
    visited = set()
    result = []

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        result.append(current)

        for neighbor, connected in enumerate(adj_matrix[current]):
            if connected and neighbor not in visited:
                stack.append(neighbor)

    return result