def warshall(graph):
    num_vertices = len(graph)
    reach = [fila[:] for fila in graph]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = 1
    return reach
