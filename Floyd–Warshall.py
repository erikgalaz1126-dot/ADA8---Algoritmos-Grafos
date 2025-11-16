def floyd(graph):
    num_vertices = len(graph)
    dist = [fila[:] for fila in graph]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

    print(fila)

