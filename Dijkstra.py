def dijkstra(graph, start):
    import math
    num_vertices = len(graph)
    dist = [math.inf] * num_vertices
    dist[start] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        min_dist = math.inf
        u = -1
        for v in range(num_vertices):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v

        visited[u] = True

        for v in range(num_vertices):
            if graph[u][v] != 0 and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
    return dist

