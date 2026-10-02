def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    result = [[0] * n for _ in range(n)]

    for key, value in adj_list.items():
        for item in value:
            result[key][item] = 1

    for row in result:
        print(row)

    return result


adjacency_list_to_matrix({
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
})